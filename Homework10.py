# Завдання 1
# Прочитайте файл data\lesson9\return_policy.txt Та напишіть простий чат бот для відповідей на питання користувачів стосовно повернення товару. Діалог завершується коли користувач вводить порожній рядок.
# Передавайте усю історію спілкування у форматі:
# Instruction: ….
# Human: massage1
# AI: message2
# Human: massage3
# AI: message4
# Human: massage5
# AI:

import os
import dotenv
import langchain
from langchain_google_genai import GoogleGenerativeAI


dotenv.load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

llm = GoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
    temperature=1
)

with open('data/lesson9/return_policy.txt', 'r', encoding='utf-8') as file:
    rules = file.read()

print(rules)

history = rules

while True:
    user_input = input('Ваше питання - ').strip()
    if user_input == '':
        break
    history += f'\n Human: {user_input}'

    response = llm.invoke(history)
    history += f'\n AI: {response}'
    print(response)
