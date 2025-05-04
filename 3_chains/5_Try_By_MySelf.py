from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")

prompt_template = ChatPromptTemplate.from_messages(
    [
        
        ("system", "You are a comedian who tells joke about {topic},  Also for every output I want you to avoid this symbol ** to make output better"),
        ("user", " Tell me a joke about {joke_count} jokes")
        
    ]
)

chain = prompt_template | model | StrOutputParser()
# chain = prompt_template | model 

result = chain.invoke({"topic" : "superman", "joke_count" : "3"})

print(f"AI : {result}")