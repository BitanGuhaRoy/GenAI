from dotenv import load_dotenv
import os
from openai import OpenAI

# Load variables from .env file
load_dotenv()


client = OpenAI()

response = client.responses.create(
    model="gpt-5.2",
    input="2+2 is equal to how much? Answer in a single word.",
)

print(response.output_text)
