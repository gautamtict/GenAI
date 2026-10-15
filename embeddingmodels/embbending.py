from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
load_dotenv()
embedding= OpenAIEmbeddings(
    model="embedding ",
    dimensions=64
)

text=[
    "hello this is akasrah",
    "hello your name"
]
vector=embedding.embed_documents(text) #for using miltipal santance

vector=embedding.embed_query("going to lern Gen Ai") #for using singal santance

print(vector)