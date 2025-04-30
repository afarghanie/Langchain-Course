# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
import os

# Load environment variables from .env
load_dotenv()

#GCP PROJECT ID

project_id = os.getenv("GOOGLE_CLOUD_PROJECT")

# Create a ChatOpenAI model
model = ChatVertexAI(model_name="gemini-2.0-flash-001", project = project_id)

# Invoke the model with a message
result = model.invoke("What is the main ide of adam smith about economy in his famous book?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
