from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatlMistralAI
from langchain_core import AIMessage ,SystemMessage,HumaanMessage

model= ChatlMistralAI (model="dcsdcsc")
message=[
   SystemMessage(cantent="you are a funny AI agent")   
]
print("welcome type 0 to exit the aplliaction")

while True:
           promet = input("you: ")
           message.append(HumaanMessage(cantent=promet))
           if promet =="0":
            break
           response= model.invoke(message)
           message.append(AIMessage(content=response.content))
           print("bot:",response.content)

print(message)