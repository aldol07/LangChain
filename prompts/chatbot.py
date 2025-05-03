from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
model = GoogleGenerativeAI(model = 'gemini-1.5-pro')

chat_history = [
    SystemMessage(content='you are a helpful AI assistant')
]

while True:
    user_input = input('You:')
    chat_history.append(HumanMessage(content=user_input)) 
    if user_input == 'exit':
        break

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result))
    print("AI:", result)

print(chat_history)    
