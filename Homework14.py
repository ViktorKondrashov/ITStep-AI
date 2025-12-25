# Завдання 1
# Напишіть чат бота, з інструментом по рекомендації ресторанів.
# Для цього скористайтесь GoogleSerperAPIWrapper(type="places")
# Інструмент повинен отримувати запит для пошуку та повертати таку інформацію про ресторани:
#  назва
#  посилання на сайт(якщо є)
#  рейтинг

import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import GoogleSerperAPIWrapper
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
serper_api_key = os.getenv("SERPER_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key=gemini_api_key,
)

searcher = GoogleSerperAPIWrapper(serper_api_key=serper_api_key,type="places")

def search_restaurant(city: str) -> str:
    """
    Шукає в інтернеті інформацію про ресторани

    :param city: назва міста
    :return: результати пошуку
    """

    results = searcher.results(f'знайдені ресторани: {city}')
    print(results)  # результати пошуку

    return results

agent = create_react_agent(
    model=llm,  # мовна модель
    tools=[search_restaurant]
)

# історія повідомлень + інструкції

messages = [
    SystemMessage(
        """
        Ти агент по пошуку інформації про ресторани. Твоя задача знайти в інтернеті інформацію про ресторани у певному місті.        
        Якщо користувач введе не назву міста, то вивести повідомлення «немає відповідної інформації»

        У тебе є доступ до таких інструментів:
        * search_restaurant -- завжди давай інформацію у вигляді: назва ресторану, посилання на сайт(якщо є), рейтинг
        """
    )
]

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