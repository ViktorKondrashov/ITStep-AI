# створення агентів
# агент -- чат-бот(llm) + інструменти

import os
import dotenv
from typing import List

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages, BaseMessage
)

# завантаження апі ключа
dotenv.load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key=gemini_api_key,
)

# модель для кодування текстів(embedding model)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=gemini_api_key
)

# створення весторної бази даних
pc = Pinecone(api_key=pinecone_api_key)
index_name = "soup"  # назва бази даних

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=768,      # кількість чисел при кодування
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
    Шукає схожі документи з релевантної інформацією до запиту користувача


    База данних містить таку інформацію:
            * інформація про Штучний Інтелект та його майбутне

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
    tools=[search_doc]
)

# історія повідомлень + інструкції

messages = [
    SystemMessage(
        """
        Ти ввічлий чат-бот. Твоя задача давати інформативні та чіткі відповіді
        на запити користувача.
        """
    )
]


# Завдання 2
# На основі створеної бази даних створіть агента та реалізуйте його у вигляді чат бота
import json
import os
import dotenv
from uuid import uuid4

# Завдання 1
# Створіть векторну базу даних, де кожен документ – це вміст файлу з папки data/lesson_rag/files
#  добавте в метадані шлях до файлу
#  створіть для кожного документу ID
#  збережіть створені ID та назви відповідних файлів в окремий json файл
# Перевірте чи працює правильно пошук

# завантаження апі ключа
dotenv.load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# модель для кодування текстів(embedding model)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=gemini_api_key
)

pc = Pinecone(api_key=pinecone_api_key)
index_name = "practice1"  # назва бази даних

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=768,      # кількість чисел при кодування
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


# інструмент -- функція
# обов'язкова документація



while True:
    user_query = input("Ви: ")

    if user_query == '':
        break

    # переводимо str рядок у  HumanMessage
    human_message = HumanMessage(user_query)

    # добавляємо повідослення користувача до історії
    messages.append(human_message)

    # застосування агента
    # треба передавати словник
    input_data = {
        "messages": messages
    }

    response = agent.invoke(input_data)
    # response -- словник з усією історією + відповідь моделі

    # отримання всіє історії повідомлень
    messages = response['messages']

    # отримати фінальну відповідь моделі
    answear = messages[-1]
    print(answear.content)

    # виведемння всієї історії
    print()
    print("Історія")

    for message in messages:
        print(repr(message))




# Завдання 3
# Внесіть зміни в декілька файлів. Змініть базу даних для цього:
#  визначте назви файлів які були змінені(вручну вказати списком в коді)
#  отримайте їхні ID
#  видаліть їх з бази даних
#  створіть нові документи та добавте в базу даних