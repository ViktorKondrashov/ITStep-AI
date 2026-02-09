from langchain_opentutorial import package
# Set environment variables

package.install(
    [
        "langchain_text_splitters",
    ],
    verbose=False,
    upgrade=False,
)

from langchain_opentutorial import set_env

set_env(
    {
        "OPENAI_API_KEY": "",
        "LANGCHAIN_API_KEY": "",
        "LANGCHAIN_TRACING_V2": "true",
        "LANGCHAIN_ENDPOINT": "https://api.smith.langchain.com",
        "LANGCHAIN_PROJECT": "RecursiveCharacterTextSplitter",
    }
)

from pdfminer.high_level import extract_text

# extract_text автоматически пытается сохранить структуру (layout)
# text = extract_text('General.pdf')
# print(text)

import docx

def get_docx_text(path):
    doc = docx.Document(path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Использование
text = get_docx_text('For wokers.docx')
# print(text)


from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    # Set the chunk size to very small. These settings are for illustrative purposes only.
    # chunk_size=250,
    # Sets the number of overlapping characters between chunks.
    chunk_overlap=50,
    # Specifies a function to calculate the length of the string.
    length_function=len,
    # Sets whether to use regular expressions as delimiters.
    is_separator_regex=False,
)

# Split the file text into documents using text_splitter.
# texts = text_splitter.create_documents([text])
texts = text_splitter.split_text(text)

print(texts.__len__())

print(texts[0])  # Outputs the first document in the split document.
print("===" * 20)
print(texts[1])  # Output the second document of the split document.



