import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

model = GoogleGenerativeAI(model="gemini-1.5-pro")

prompt = PromptTemplate(
    template="Answer the following question:\n{question}\nFrom the following text:\n{text}",
    input_variables=["question", "text"]
)

parser = StrOutputParser()

url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421"


loader = WebBaseLoader(url)
docs = loader.load()

# Create the LangChain pipeline
chain = prompt | model | parser


response = chain.invoke({
    "question": "What is the product that we are talking about?",
    "text": docs[0].page_content
})


print("\n🧠 Answer:")
print(response)
