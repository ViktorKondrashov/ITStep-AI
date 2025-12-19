# Завдання 1
# Напишіть чат модель яка підсумовує всю розмову в декілька речень. Вкажіть щоб модель зберігала якомога більше деталей.
# Використайте цю модель для простого чат бота який замість trim_massages використовує модель з підсумуванням.
# Підсумовуйте повідомлення, коли їх більше 4.
# Старі повідомлення треба видалити
# НЕ ВИДАЛЯТИ SystemMessage та не використовувати його для підсумування

import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages,
    BaseMessage
)

from typing import List, Union
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import  PromptTemplate


# завантаження апі ключа
dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

messages: List[BaseMessage] = [
    SystemMessage("""
    Ти співрозмовник, яка підсумовує всю розмову в декілька речень. Зберігай якомога більше деталей.    
    Підсумовуй повідомлення, коли їх більше 4. Не використовуй SystemMessage для підсумування розмови.
    """)
]

trimmer = trim_messages(
    strategy='last',  # залишати останні повідомлення

    token_counter=len,  # рахуємо кількість повідомлень
    max_tokens=15,  # залишати максимум 15 повідомлення(System, AI, Human)

    start_on='human',  # історія завжди починатиметься з HumanMessage
    end_on='human',  # історія завжди закінчуватиметься з HumanMessage
    include_system=True  # SystemMessage не чіпати
)

chain = trimmer | llm

while True:
    user_query = input("Ваше повідомлення: ")
    messages.append(HumanMessage(user_query))

    if user_query == '':
        break

    response = chain.invoke(messages)
    messages.append(response)

    for m in messages:
        print(repr(m))

    print(f"AI: {response.content}")
