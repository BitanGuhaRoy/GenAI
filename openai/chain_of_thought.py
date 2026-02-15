import string
from dotenv import load_dotenv
import os
from openai import OpenAI
import json
# Load variables from .env file
load_dotenv()
#chain of thought 
# Chain of thought prompting is a technique where we ask the model to explain its reasoning process step by step before giving the final answer.
#  This can help the model to arrive at the correct answer by breaking down the problem into smaller parts and reasoning through them.

# @TODO: Add more examples of chain of thought prompting. 
client = OpenAI()

SYSTEM_PROMPT = """
You are an AI assistant that works in incremental steps.

Rules:
1. Always respond in valid JSON
2. Response format:
   {
     "step": "START" | "PLAN" | "OUTPUT",
     "content": "string"
   }
3. Do NOT output multiple steps at once
4. Only produce the NEXT logical step
5. Assume previous steps are already stored by the user

"""


response = client.chat.completions.create(
    model="gpt-5-nano",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "What is 7*8+19 ?"}
    ],
)   

print(response.choices[0].message.content)

