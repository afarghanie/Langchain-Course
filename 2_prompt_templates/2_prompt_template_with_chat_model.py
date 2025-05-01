from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")

# PART 1: Create a ChatPromptTemplate using a template string
# print("-----Prompt from Template-----")
# template = "Tell me a joke about {topic}."
# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({"topic": "cats"})
# result = model.invoke(prompt)
# print(result.content)

# PART 2: Prompt with Multiple Placeholders
# print("\n----- Prompt with Multiple Placeholders -----\n")
# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} short story about a {animal}.
# Assistant:"""
# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})

# result = model.invoke(prompt)
# print(result.content)

# PART 3: Prompt with System and Human Messages (Using Tuples)
# print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}."),
#     ("human", "Tell me {joke_count} jokes."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
# result = model.invoke(prompt)
# print(result.content)

# Part 4 Trying Myself "String Prompt Templates"
# print("--String Prompt Templates")
# prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")

# prompt = prompt_template.invoke({"topic": "cats"})
# result = model.invoke(prompt)
# response = result.content

# print(f"AI Response : {response}")

# Part 5 Trying Myself using #Chat Prompt Templates
print("--Chat Prompt Template--")

prompt_template = ChatPromptTemplate([("system","You are helpful AI asistant"),("user", "Tell me a joke about {Topic}")])
prompt = prompt_template.invoke({"Topic" : " Crocodile"})
result = model.invoke(prompt)
response = result.content

print(f"AI : {response}")

