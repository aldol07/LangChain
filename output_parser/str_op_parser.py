from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini
model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro')

# Step 1: Detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# Step 2: 5-line summary
template2 = PromptTemplate(
    template='Write a 5-line summary of the following text:\n{text}',
    input_variables=['text']
)

# Step 1: Generate report
prompt1 = template1.format(topic='black hole')
result = model.invoke(prompt1)

# Step 2: Generate summary
prompt2 = template2.format(text=result.content)
result1 = model.invoke(prompt2)

print("=== Detailed Report ===")
print(result.content)

print("\n=== 5-Line Summary ===")
print(result1.content)
