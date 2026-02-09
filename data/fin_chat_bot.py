import streamlit as st

import sqlite3

import requests
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool


def get_engine_for_chinook_db():
    """Pull sql file, populate in-memory database, and create engine."""
    url = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql"
    response = requests.get(url)
    sql_script = response.text

    connection = sqlite3.connect(":memory:", check_same_thread=False)
    connection.executescript(sql_script)
    return create_engine(
        "sqlite://",
        creator=lambda: connection,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )


engine = get_engine_for_chinook_db()

db = SQLDatabase(engine)


# за замовчуванням щапускається нескіченний цикл
# Сторінка сайту постійно оновлюється і відповідно
# код нижче постіно запускається

# # заголовок сайту
# st.title("IT STEP ai")
#
# # звичайний текст
# st.markdown("Звичайний текст. Можливо опис вашої програми")
#
# # отримати повідомлення від користувача
# user_query = st.chat_input("Ваше повідомлення")
#
# # st.markdown(f"Ви ввели {user_query}")
# #
# # if user_query == 'Привіт':
# #     st.markdown(f"Як справи")
#
#
# # глобальна пам'ять в streamlit
# # session_state -- dict з зміними
#
# if user_query == None:
#     # це самий початок(користувач ще нічого не писав
#     st.session_state['history'] = []
#
# # добавити user_query в історію
# st.session_state['history'].append(user_query)
#
# st.markdown(f"Ви ввели {st.session_state['history']}")

# ЧАТ-БОТ

import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

# заголовок
st.title("Final project hospital chat bot")

# завантаження апі ключа за допомогою streamlit
api_key = st.secrets.get("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# створення агента
agent = create_react_agent(
    model=llm,  # мовна модель
    tools=[]
)

user_query = st.chat_input("Ваше повідомлення")

# якщо це початок то створити історію в session state
if user_query is None:
    # історія повідомлень
    st.session_state['history'] = [
        # перше повідомлення з основними інструкціями(промпт)
        SystemMessage(
            """
            Ти -- ввічливий чат бот, твоя задача давити короткі та
            чіткі відповіді на питання
            """
        )
    ]

# якщо повідомлення введено, то дати відповідь від моделі
if user_query:
    # переволимо повідомлення в HumanMessage
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