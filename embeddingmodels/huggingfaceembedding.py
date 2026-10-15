from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(
    model="asdasdasdasd",

)
text=[
    "hello this is akasrah",
    "hello your name"
]

vecter = embedding.embed_documents(text)