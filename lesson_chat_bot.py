import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages
)


# завантаження апі ключа
dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

# # історія повідомлень
# messages = [
#     # перше повідомлення з основними інструкціями(промпт)
#     SystemMessage(
#         """
#         Ти -- ввічливий чат бот, твоя зада давити короткі та
#         чіткі відповіді на питання
#         """
#     ),
#     HumanMessage("Привіт"),
#     AIMessage("Привіт, щоб ти зотів дізнатись?"),
#     HumanMessage("Порекомендуй цікавий фільм про космос")
# ]
#
#
# # дати відповідь на очтаннє повідомлення
# # враховуючи історію спілкування та основні інструкції
#
# response = llm.invoke(messages)
#
# print(type(response))
# print(response)
# print(repr(response))


# простий чатбот

# історія повідомлень
# на початку лише інструкції
# messages = [
#     SystemMessage(
#         """
#         Ти -- ввічливий чат бот, який імітує Толкіна. Давай короткі відповіді
#         на питання користувача
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     # закіцнчуємо якщо натиснути Enter
#     if user_query == '':
#         break
#
#     # переволимо повідомлення в HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо до історії повідомлень
#     messages.append(human_message)
#
#     # запускаємо модель
#     response = llm.invoke(messages)
#
#     # response -- AIMessage
#     # добавляємо до історії повідомлень
#     messages.append(response)
#
#     # вивести відповідь
#     print(f"AI: {response.content}")
#
#     # вивести саму історії спілкування
#     print()
#     print("####ІСТОРІЯ####")
#
#     for message in messages:
#         print(repr(message))
#
#     print()


# очищення історії

# # створення трімера повідомлень
# trimmer = trim_messages(
#     strategy='last',  # залишати останні повідомлення
#
#     token_counter=len,  # рахуємо кількість повідомлень
#     max_tokens=5,  # залишати максимум 5 повідомлення(System, AI, Human)
#
#     start_on='human',  # історія завжди починатиметься з HumanMessage
#     end_on='human',  # історія завжди закінчуватиметься з HumanMessage
#     include_system=True  # SystemMessage не чіпати
# )
#
# messages = [
#     SystemMessage(
#         """
#         Ти -- ввічливий чат бот, який імітує Толкіна. Давай короткі відповіді
#         на питання користувача
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     # закіцнчуємо якщо натиснути Enter
#     if user_query == '':
#         break
#
#     # переволимо повідомлення в HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо до історії повідомлень
#     messages.append(human_message)
#
#     # застововуємо трімер
#     messages = trimmer.invoke(messages)
#
#     # запускаємо модель
#     response = llm.invoke(messages)
#
#     # response -- AIMessage
#     # добавляємо до історії повідомлень
#     messages.append(response)
#
#     # вивести відповідь
#     print(f"AI: {response.content}")
#
#     # вивести саму історії спілкування
#     print()
#     print("####ІСТОРІЯ####")
#
#     for message in messages:
#         print(repr(message))
#
#     print()

# можна зробити ланцюг

# створення трімера повідомлень
# trimmer = trim_messages(
#     strategy='last',  # залишати останні повідомлення
#
#     token_counter=len,  # рахуємо кількість повідомлень
#     max_tokens=5,  # залишати максимум 5 повідомлення(System, AI, Human)
#
#     start_on='human',  # історія завжди починатиметься з HumanMessage
#     end_on='human',  # історія завжди закінчуватиметься з HumanMessage
#     include_system=True  # SystemMessage не чіпати
# )
#
# # створити ланцюг
# chat_chain = trimmer | llm
#
# messages = [
#     SystemMessage(
#         """
#         Ти -- ввічливий чат бот, який імітує Толкіна. Давай короткі відповіді
#         на питання користувача
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     # закіцнчуємо якщо натиснути Enter
#     if user_query == '':
#         break
#
#     # переволимо повідомлення в HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо до історії повідомлень
#     messages.append(human_message)
#
#     # запускаємо ланцюг
#     response = chat_chain.invoke(messages)
#
#     # response -- AIMessage
#     # добавляємо до історії повідомлень
#     messages.append(response)
#
#     # вивести відповідь
#     print(f"AI: {response.content}")
#
#     # вивести саму історії спілкування
#     print()
#     print("####ІСТОРІЯ####")
#
#     for message in messages:
#         print(repr(message))

    # print()

    # Завдання    2
    # Напишіть    чат    бота, який    дає    відповіді    на    питання    стосовно    умов    повернення    товару.
    # Якщо    користувач    запитує    щось    інше, то    відповідати    що    немає    інформації.
    # Застосуйте    обмеження    історії(можна    десь    5    повідомлень)

with open(r'data/lesson9/return_policy.txt','r',encoding='utf-8') as file:
    return_policy = file.read()

messages = [SystemMessage(f"""
    Ти консультант магазину, який допомогає покупцю с поверненням товару та консультує щодо його умов.
    Якщо    покупець    запитує    щось    інше, то    відповідати    що    немає    інформації.
    
    ### УМОВИ ПОВЕРНЕННЯ
    {return_policy}
    
""")]

trimmer = trim_messages(
    strategy='last',  # залишати останні повідомлення

    token_counter=len,  # рахуємо кількість повідомлень
    max_tokens=11,  # залишати максимум 5 повідомлення(System, AI, Human)

    start_on='human',  # історія завжди починатиметься з HumanMessage
    end_on='human',  # історія завжди закінчуватиметься з HumanMessage
    include_system=True  # SystemMessage не чіпати
)

while True:
    user_message = input('Ви:')

    if user_message == '':
        break

    human_message = HumanMessage(user_message)

    messages.append(human_message)

    messages = trimmer.invoke(messages)

    response = llm.invoke(messages)

    print('AI:', response.content)

    messages.append(response)



