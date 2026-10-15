from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)

modul=ChatHuggingFace(llm=llm)
response = modul.invoke("who are you")
print(response.content)