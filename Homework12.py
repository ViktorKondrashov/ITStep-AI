# Завдання 1
# Напишіть модель для генерації персонального плану тренувань з двох ланцюгів:
#  Перший ланцюг отримує мету тренування(схуднення, набір м’язів, тощо) та повертає список вправ
#  Другий ланцюг отримує список вправ, рівень підготовки користувача(низький, середній, професіонал) та кількість часу на тиждень(в годинах) і повертає план тренувань

import os
import dotenv

from typing import List
from pydantic import BaseModel, Field
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from transformers.utils.chat_template_utils import description_re

# завантаження апі ключа
dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# створити llm
llm = GoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key=api_key,
)

def get_list_exercises_chain():
    # структура відповіді
    class ParserResult(BaseModel):
        exercises: List[str] = Field(description='список вправ')

    # # створення парсера
    parser = PydanticOutputParser(pydantic_object=ParserResult)
    instructions = parser.get_format_instructions()

    # промпт
    prompt = PromptTemplate.from_template(
        """
        Ты - фітнес-тренер. Тобі потрібно підібрати список вправ відповідно до мети тренування користувача.
 
        ### МЕТА ТРЕНУВАННЯ
        {user_target}

        ### ІНСТРУКЦІІ
        {instructions}

        """,
        partial_variables={"instructions": instructions}
    )

    chain = prompt | llm | parser

    return chain


def get_training_plan_chain():
    # промпт
    prompt = PromptTemplate.from_template(
        """
        Ты - фітнес-тренер. Тобі потрібно створити план тренувань на підставі списка вправ,
        рівня підготовки користувача(низький, середній, професіонал) та кількісті часу на тиждень(в годинах)

        ### РІВЕНЬ ПІДГОТОВКИ
        {user_level}
        
        ### КІЛЬКІСТЬ ЧАСУ НА ТИЖДЕНЬ(В ГОДИНАХ)
        {time}
        

        ### СПИСОК ВПРАВ
        {list_exercises}
        """
    )

    chain = prompt | llm

    return chain


user_target = input("Мета тренування: ")
user_level = input("Рівень підготовки: ")
time = input("Кількість часу на тиждень(в годинах): ")


list_exercises_chain = get_list_exercises_chain()

list_exercises_response = list_exercises_chain.invoke({
    "user_target": user_target
})

training_plan_chain = get_training_plan_chain()

training_plan_response = training_plan_chain.invoke({
    "user_level": user_level,
    "time": time,
    "list_exercises": list_exercises_response.exercises
})

print(training_plan_response)
