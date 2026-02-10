from typing import List

import streamlit as st

import requests
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

import os
import dotenv

from sqlalchemy import create_engine
# from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document



# Load environment variables from .env
load_dotenv()
pinecone_api_key = os.getenv("PINECONE_API_KEY")


# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

engine = create_engine(DATABASE_URL)

# try:
#     with engine.connect() as connection:
#         print("Connection successful!")
# except Exception as e:
#     print(f"Failed to connect: {e}")

db = SQLDatabase(engine)


# ЧАТ-БОТ


# заголовок
st.title("Final project hospital chat-bot")

# завантаження апі ключа за допомогою streamlit
api_key = st.secrets.get("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

listtools = toolkit.get_tools()

# модель для кодування текстів(embedding model)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)

pc = Pinecone(api_key=pinecone_api_key)
index_name = "hospital"  # назва бази даних

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=3072,      # кількість чисел при кодування
        metric="cosine",    # формула для схожості
        spec=ServerlessSpec(
            cloud="aws",         # хмарний сервер(амазон)
            region="us-east-1"   # регіон(Каліфорнія)
        ),
    )

index = pc.Index(index_name)
vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)


def search_doc(user_query: str) -> List[Document]:
    """
    Шукає схожі документи з релевантною інформацією до запиту користувача


    База даних містить таку інформацію:
            * інформація про умови користування гуглом

    :param user_query: запит користувача
    :return: список документів з релевантною інформацією
    """
    result_docs = vector_store.similarity_search(
        user_query,  # текст для порівняння схожості
        k=3,  # кількість документів у відповіді
    )

    return result_docs


# створення агента
agent = create_react_agent(
    model=llm,  # мовна модель
    tools=toolkit.get_tools()
)

user_query = st.chat_input("Ваше повідомлення")

# якщо це початок то створити історію в session state
if user_query is None:
    # історія повідомлень
    st.session_state['history'] = [
        # перше повідомлення з основними інструкціями(промпт)
        SystemMessage(
            """
            Ти -- ввічливий чат бот, який працює с базою даних SQL. Твоя задача давати короткі та
            чіткі відповіді на питання. У тебе є доступ до інструментів
            для роботи з базою даних. Нижче інструкція для роботи з нею.
               You are an agent designed to interact with a SQL database.Given an input question,
            create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
            Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
            You can order the results by a relevant column to return the most interesting examples in the database.
            Never query for all the columns from a specific table, only ask for the relevant columns given the question.
            You have access to tools for interacting with the database.Only use the below tools.
            Only use the information returned by the below tools to construct your final answer.
            You MUST double check your query before executing it. If you get an error while executing a query,
             rewrite the query and try again.DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
             To start you should ALWAYS look at the tables in the database to see what you can query.
             Do NOT skip this step.Then you should query the schema of the most relevant tables.
            
            """
        )
    ]

# якщо повідомлення введено, то дати відповідь від моделі
if user_query:
    # переводимо повідомлення в HumanMessage
    human_message = HumanMessage(user_query)

    # добавляємо до історії повідомлень
    st.session_state['history'].append(human_message)

    input_data = {
        'messages':st.session_state['history']
    }

    # запускаємо модель
    response = agent.invoke(input_data)

    # response -- AIMessage
    # добавляємо до історії повідомлень
    st.session_state['history'] = response['messages']

# вывод всей истории общения
for message in st.session_state['history']:
    if isinstance(message, SystemMessage):
        continue

    # содержание сообщения
    text = message.content

    # получить роль
    if isinstance(message, HumanMessage):
        role = "human"

    else:
        role = "ai"

    with st.chat_message(role):
        st.markdown(text)