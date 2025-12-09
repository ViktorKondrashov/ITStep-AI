# LLM
# Large Language Model
# велика мовна модель

# завантеження api key як змінну середовища
import os
import dotenv

# завантаження даних з файлу .env
dotenv.load_dotenv()

# сам api key
api_key = os.getenv('GEMINI_API_KEY')

# сама модель LMM
import langchain
from langchain_google_genai import GoogleGenerativeAI

# root/
#   - langchain.py
#   - langchain_google_genai.py

# # створення моделі
# llm = GoogleGenerativeAI(
#     model='gemini-2.5-flash-lite',   # назва моделі
#     api_key=api_key
# )
#
# # запуск моделі
# response = llm.invoke('Привіт, що таке LLM?')
#
# print(response)


# Як це працює

# Запит: Привіт, що таке LLM?
# Шматок Відповіді: Привіт! LLM

# Завдання моделі -- згенерувати наступне слово
# Для кожного відомого слова генеруються ймовірності
# розшивровується  - 30%
# це               - 25%
# використовується - 10%
# яблуко           - 0.0000000001%


# параметри креативності
llm = GoogleGenerativeAI(
    model='gemini-2.5-flash-lite',   # назва моделі
    api_key=api_key,
    top_k=10,   # вибрати випадково наступне слово з 10 з найбільшою ймовірністю
    top_p=0.8,  # залишити ті слова, сума ймовірностей яких не менше 80%, та вибирати серед них
    temperature=1.5  # вища температура -- відсотки стають більш однаковими
)

# temperature
# 0 - 0.3    -- низька креативність(відповіді як по методичці)
# 0.7 - 1.2  -- середня креативність(відповідає як людина)
# 1.5-1.7    -- висока креативність(вигадає щось цікаве або збреше)
# >2         -- випадкові слова


# Завдання 1
# Підключіть модель LLM за допомогою свого API key.
# Попросіть модель згенерувати:
# ● відповідь на питання у вигляді одного
# слова(наприклад яка столиця Франції?)
# ● код python
# ● коротку історію
# Підберіть параметри креативності та довжини

import os
import dotenv
from langchain_google_genai import GoogleGenerativeAI


dotenv.load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')

llm = GoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    temperature=0
)

user_input = input('Your question: ')
# command1 = 'дай ответ одним словом. если ответ два и больше слова, то давай полный ответ. '
# command_py = 'write response of the python code (only): '
command_story = 'write story within 4 sentences. be creative and fun. '

response = llm.invoke(command_story + user_input)
print(response)

# # create a model
# llm = GoogleGenerativeAI(
#     model='gemini-2.5-flash-lite', # model name
#     api_key=api_key,
#     top_k=1, # choose random next word from 10 with greater probability
#     top_p=0.8, # leave words, which probability sum not greater 80% and choose avg
#     temperature=2, # the higher the temperature - the more similar the percentages become
# )

# start model
# ● відповідь на питання у вигляді одного слова(наприклад яка столиця Франції?)
# response = llm.invoke('Give response with only one word. Tell me France capital name')

# ● код python
# response = llm.invoke('Give me Python code for sum 2 numbers, for example 3+2')

# ● коротку історію
# response = llm.invoke('Напиши историю о программисте, который попал в лес')
# print(response)

# Завдання 2
# Прочитайте файл data\lesson9\rules.txt з правилами користування атракціону.
# Напишіть програму яка отримує від користувачі питання та дає відповідь на нього виходячи з текстового файлу.
# Для цього об’єднайте правила користування з питанням користувача.
# Користувач задає питання поки не введе порожній рядок.
# Змініть файл rules.txt, щоб переконатись що модель дійсно його читає.

# with open('data/lesson9/rules.txt', 'r', encoding='utf-8') as file:
#     rules = file.read()
#
# user_question = input("enter question: ")
#
# response = llm.invoke(f'{rules} Вопрос: {user_question}. Дай ответ только по правилам. '
#                       f'Дай ответ тем же языком, на котором был задан вопрос')
# print(response)


#Завдання 3

# Створіть найпростіший чат бот. Напишіть моделі якого персонажа вона повинна вдавати(відомий актор, персонаж кіно\книги, тощо).
# Реалізуйте двома способами:
# 1. Модель отримує інструкцію в якому стилі відповідати та нове повідомлення.
# 2. Модель отримує інструкцію та історію попередніх повідомлень як від користувача, так і її власні відповіді у форматі
# Instruction: ….
# Human: massage1
# AI: message2
# Human: massage3
# AI: message4
# Human: massage5
# AI:

# llm = GoogleGenerativeAI(
#     model='gemini-2.5-flash-lite',
#     api_key=api_key,
#     temperature=1
# )
#
#
# history = 'Відповідай як Джекі Чан'
#
# while True:
#     user_input = input('Ваше питання - ')
#     history += f'\n Human: {user_input}'
#
#
#     response = llm.invoke(history)
#     history += f'\n AI: {response}'
#     print(response)


