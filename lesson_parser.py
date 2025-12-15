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


# Користувач задає питання.
# Потрібно дати відповіть та запропопонувати цікаві факти по тій
# же темі що і питання

# # варіант 1 -- все в один промпт
# prompt = PromptTemplate.from_template(
#     """
#     Ти -- чатбот для навчання. Твоя задача давати відповідь на питання.
#     Також потрібно запропонувати декілька цікавих фактів по тій же темі
#     що і питання
#
#     ### Питання
#     {question}
#     """
# )
#
# chain1 = prompt | llm
#
# response = chain1.invoke({
#     "question": "Коли була висадка на місяць"
# })
#
# print(response)


# варіант 2 -- розьити на 2 кроки
# дати відповідь та визначити тему питання
# згенерувати цікаві факти по темі

# пишемо парсер

# структура відповіді
# class ParserResult(BaseModel):
#     question_answer: str = Field(description="Answer to user question")
#     topics: List[str] = Field(description="список пов'язаних тем до питання")
#
#
# # створення парсера
# parser = PydanticOutputParser(pydantic_object=ParserResult)
#
# # інструкція для llm як має виглядати відповідь
# instructions = parser.get_format_instructions()
#
# prompt = PromptTemplate.from_template(
#     """
#     Ти -- чатбот для навчання. Твоя задача давати відповідь на питання.
#     Також потрібно визначити теми які відносяться до цього питання
#
#     ### Питання
#     {question}
#
#     ### ФОРМАТ ВІДПОВІДІ
#     {instructions}
#     """,
#     partial_variables={"instructions": instructions}  # одразу передаємо інструкції
# )
#
# chain = prompt | llm | parser
#
# question = input("Введіть питання: ")
#
# response = chain.invoke({
#     "question": question,
# })
#
# print(f"Відповідь: {response.question_answer}")
#
#
# # print(response)
# # print(type(response))
# #
# # print(response.question_answer)
# # print(response.topics)
#
# # генерація цікавих фактів на основі тем
# class FactResponse(BaseModel):
#     facts: List[str] = Field(description="список цікавих фактів розом з їхнім описом")
#
#
# # створення парсера
# parser = PydanticOutputParser(pydantic_object=FactResponse)
#
# # інструкція для llm як має виглядати відповідь
# instructions = parser.get_format_instructions()
#
# prompt = PromptTemplate.from_template(
#     """
#     Ти -- генератор цікавих фактів. Твоя задача навести 5 цікавих фактів
#     на задані теми
#
#     ### ТЕМИ
#     {topics}
#
#     ### ФОРМАТ ВІДПОВІДІ
#     {instructions}
#     """,
#     partial_variables={"instructions": instructions}  # одразу передаємо інструкції
# )
#
# chain2 = prompt | llm | parser
#
# response = chain2.invoke(
#     {
#         "topics": response.topics
#     }
# )
#
# facts = response.facts
#
# print("Цікаві факти")
# for fact in facts:
#     print(fact)
#
# whole_chain = chain | chain2
#
# # Завдання 1
# # Напишіть модель для рекомендації книг з двох ланцюгів
# #  Перший ланцюг отримує назву книги та визначає її жанр
# #  Другий отримує назву книги, жанр та повертає список
# # схожих книг(того ж самого жанру та іншого)
#
# import os
# import dotenv
# from typing import List
# from pydantic import BaseModel, Field
# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.output_parsers import PydanticOutputParser
#
#
# dotenv.load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")
#
# llm = GoogleGenerativeAI(
#     model='gemini-2.5-flash',
#     api_key=API_KEY,
#     temperature=0
# )
#
# class BookInfo(BaseModel):
#     genre: str = Field(description='жанр книги')
#
# parser = PydanticOutputParser(pydantic_object=BookInfo)
#
# instructions = parser.get_format_instructions()
#
# prompt = PromptTemplate.from_template("""Ти - бібліотекар. Твоє завдання полягає в тому, щоб визначати жанри книг.
# ### ІСТРУКЦІЇ
# {instructions}
#
# ### НАЗВА КНИГИ
# {book_title}"""
# , partial_variables={'instructions': instructions})
#
# chain1 = prompt | llm | parser
#
# user_book = input('Введіть назву книги ')
#
# response = chain1.invoke({
#     'book_title': user_book
# })
#
# class UpgradedBookInfo(BaseModel):
#     books: List[str] = Field(description='список схожих книг')
#
# parser = PydanticOutputParser(pydantic_object=UpgradedBookInfo)
#
# instructions = parser.get_format_instructions()
#
# prompt = PromptTemplate.from_template("""Ти - бібліотекар. Твоє завдання полягає в тому, щоб радити подібні книги на основі назви книги та жанру.
# ### ІСТРУКЦІЇ
# {instructions}
#
# ### НАЗВА КНИГИ
# {book_title}
#
# ### ЖАНР
# {book_genre}""", partial_variables={'instructions': instructions})
#
# chain1 = prompt | llm | parser
#
# full_response = chain1.invoke({
#     'book_title': user_book,
#     'book_genre': response.genre
# })
#
# for book in full_response.books:
#     print(book)


# Завдання 2
# Напишіть модель для генерації листа:
# Перший ланцюг отримує короткий опис листа та генерує основний зміст
# Другий ланцюг отримує основний зміст та стиль листа(формальний, неформальний, тощо) та генерує лист

# завантажити api ключі з папки .env
dotenv.load_dotenv()

# отримати сам ключ
api_key = os.getenv('GEMINI_API_KEY')

# створити llm
llm = GoogleGenerativeAI(
    model='gemini-2.5-flash-lite',  # назва моделі
    api_key=api_key,  # ваша API
)


def get_content_chain():
    # структура відповіді
    class ParserResult(BaseModel):
        content: str = Field(description="Здесь текст сообщения по данным")

    # # створення парсера
    parser = PydanticOutputParser(pydantic_object=ParserResult)
    instructions = parser.get_format_instructions()

    # промпт
    prompt = PromptTemplate.from_template(
        """
        Ты - помощник по составлению писем. Тебе нужно составить текст по описанию, которое напишет пользователь

        #Сообщение от пользователя
        {user_text}

        #ИНСТРУКЦИИ
        {instructions}

        """,
        partial_variables={"instructions": instructions}
    )

    chain = prompt | llm | parser

    return chain


def get_letter_chain():
    # промпт
    prompt = PromptTemplate.from_template(
        """
        Ты - помощник по составлению писем. Тебе нужно изменить содержание сообщения под стиль

        #СТИЛЬ СООБЩЕНИЯ
        {user_style}

        #СОДЕРЖАНИЕ
        {content}
        """
    )

    chain = prompt | llm

    return chain


user_text = input("Опишите содержание: ")
user_style = input("Опишите cтиль содержания: ")

content_chain = get_content_chain()

content_response = content_chain.invoke({
    "user_text": user_text
})

letter_chain = get_letter_chain()

letter_response = letter_chain.invoke({
    "user_style": user_style,
    "content": content_response.content
})

print(letter_response)


# Завдання 3
# Напишіть модель для генерації резюме:
#  Перший ланцюг отримує опис вакансії та повертає основні навички, які необхідні
#  Другий ланцюг отримує основні навички та опис кандидата і генерує резюме

description = """

## Job Title: Data Scientist

### Location:

Remote / Kyiv, Ukraine (flexible)

### About the Company:

We are an innovative tech company leveraging data and AI to build impactful products. Our mission is to transform data into actionable insights that drive business and product decisions.

### Job Description:

We are seeking a Data Scientist to analyze large datasets, develop predictive models, and support data-driven decision-making across the organization. You will work closely with product, engineering, and analytics teams to uncover insights, optimize processes, and deliver business value.

### Responsibilities:

* Analyze structured and unstructured datasets to uncover patterns and insights.
* Develop, validate, and deploy predictive and prescriptive models.
* Collaborate with engineers and product teams to integrate machine learning models into applications.
* Design experiments, perform statistical analysis, and generate actionable insights.
* Visualize data and communicate findings effectively to stakeholders.
* Stay up-to-date with the latest trends in machine learning, AI, and data analytics.

### Requirements:

* Strong knowledge of Python, SQL, and data manipulation libraries (Pandas, NumPy, etc.).
* Experience with machine learning frameworks (scikit-learn, TensorFlow, PyTorch, etc.).
* Solid understanding of statistics, probability, and data modeling.
* Experience with data visualization tools (Matplotlib, Seaborn, Plotly, Tableau, etc.).
* Strong problem-solving skills and analytical mindset.
* Excellent communication skills, able to explain technical concepts to non-technical stakeholders.

### Nice to Have:

* Experience with NLP, computer vision, or deep learning projects.
* Experience with big data tools (Spark, Hadoop, BigQuery).
* Familiarity with cloud platforms (GCP, AWS, Azure) and ML pipelines.
* Knowledge of experiment design and A/B testing.

### Benefits:

* Competitive salary and performance bonuses.
* Remote-first, flexible working environment.
* Opportunities to work on cutting-edge AI and analytics projects.
* Professional growth and learning opportunities.
* Collaborative and supportive team culture.

"""
class HRResponse(BaseModel):
    skills: List[str] = Field(description='основні навички')

parser =PydanticOutputParser(pydantic_object=HRResponse)

instructions = parser.get_format_instructions()

prompt = PromptTemplate.from_template("""
    Ти - рекрутер. Твоє завдання описати основні навички, необхідні претенденту на вакансію.
    
### ІНСТРУКЦІІ
{instructions}

### ОПИС ВАКАНСІЇ
{description}
    
""", partial_variables={'instructions': instructions})

chain_skills = prompt | llm | parser

full_response = chain_skills.invoke({
    'description': description
})

print(full_response.skills)