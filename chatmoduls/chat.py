from dotenv import load_dotenv
load_dotenv()
# import os

from langchain.chat_models import init_chat_model

# os.environ["OPENAI_API_KEY"] = "sk-..."

model = init_chat_model("gpt-5.5")

response = model.invoke("what is cricket")
print(response)


# MISTRAL  llm modul free 