import json
import os
import dotenv
from uuid import uuid4
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

# Завдання 1
# Добавте в створену базу даних файл data/lesson_rag/huge_file.txt про умови користування гуглом
# Оскільки файл надто великий, то його треба добавляти частинами. Для цього:
#  прочитайте вміст файлу
#  розділіть його на окремі блоки(між блоками два порожніх рядка, дивись файл)
#  отримайте перший рядок кожного блоку – це його назва
#  створіть документи для кожного блоку. В метаданих:
# o назва файлу
# o назва блоку
#  створіть ID та добавте все в існуючу базу даних
#  добавте ID у json файл
#  перевірте агента


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

pc = Pinecone(api_key=pinecone_api_key)
index_name = "homework15"  # назва бази даних

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

f = open("data/lesson_rag/huge_file.txt", "rt", encoding='utf-8')
text = f.read()
blocks = text.split("\n\n\n")

docs = []
for block in blocks:
    doc = Document(
        page_content=block,  # вміст документа
        metadata={'name': f.name,
                  'name_block': block.splitlines()[0]
                  }
    )
    docs.append(doc)

f.close()

#creating unique documents id
ids = [str(uuid4()) for _ in  range(len(docs))]

id_map = {}

for doc,id  in  zip(docs, ids):
    id_map[doc.metadata["name_block"]] = id

print(id_map)

with open ('ids.json', 'w') as f:
    json.dump(id_map, f, indent=2)

# #завантаження документів у базу даних
vector_store.add_documents(
    documents=docs,
    ids=ids
)

def search_doc(user_query: str) -> List[Document]:
    """
    Шукає схожі документи з релевантною інформацією до запиту користувача


    База даних містить таку інформацію:
            * інформація про умови користування гуглом

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
