# Завдання 1
# Напишіть додаток з чат ботом по допомозі з вивченням англійської мови.
#  Якщо користувач просить перекласти слово або фразу, то вивести переклад та приклад використання у речені
#  Якщо користувач просить перекласти речення, то вивести переклад та пояснення граматики, наприклад структура there is/are, пасивна форма дієслова, тощо

import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

# заголовок
st.title("Translator chat bot")

api_key = st.secrets.get("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

user_query = st.chat_input("Ваше повідомлення")

if user_query is None:
    # історія повідомлень
    st.session_state['history'] = [
        SystemMessage(
            """
            Ти -- ввічливий чат бот, твоя задача допомогати з вивченням англійської мови.
            Якщо користувач просить перекласти слово або фразу, виведи переклад та приклад використання у реченні.
            Якщо користувач просить перекласти речення, виведи переклад та пояснення граматики, наприклад: структура there is/are, пасивна форма дієслова, тощо.
            """
        )
    ]

if user_query:
    human_message = HumanMessage(user_query)

    st.session_state['history'].append(human_message)

    response = llm.invoke(st.session_state['history'])

    st.session_state['history'].append(response)

for message in st.session_state['history']:
    if isinstance(message, SystemMessage):
        continue

    text = message.content

    if isinstance(message, HumanMessage):
        role = "human"
    else:
        role = 'ai'

    with st.chat_message(role):
        st.markdown(text)