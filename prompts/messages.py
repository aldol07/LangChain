from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()
model = GoogleGenerativeAI(model = 'gemini-1.5-pro')

messages = [
    SystemMessage(content='You are ahelpful assistant'),
    HumanMessage(content='Tell me about Langchain'),
    
]

result = model.invoke(messages)
messages.append(AIMessage(content = result))

print(messages)
