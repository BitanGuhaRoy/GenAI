from dotenv import load_dotenv
import os
from openai import OpenAI

# Load variables from .env file
load_dotenv()


client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-5-nano",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant. Who can answer only mathematical questions, if user asks non mathematical question, you will respond with 'I can only answer mathematical questions.'"},
#         {"role": "user", "content": "Who is Narendra modi ?"}
#     ],
# )


# print(response.choices[0].message.content)

#zero shot prompting 
#just ask question it will reply that's it. 


# SYSTEM_PROMPT = "You are a helpful assistant. Who can answer only mathematical questions," \
#         " if user asks non mathematical question, " \
#         " you will respond with 'I can only answer mathematical questions.'"
 
# response = client.chat.completions.create(
#     model="gpt-5-nano",
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Who is Narendra modi ?"}
#     ],
# )
# print(response.choices[0].message.content)



#Few shot prompting
#Give example to the model in the prompt and then ask question, this is called few shot prompting.
#  Few shot prompting is more effective than zero shot prompting.
# SYSTEM_PROMPT = "You are a helpful assistant. Who can answer only mathematical questions," \
#         " if user asks non mathematical question, " \
#         " you will respond with 'I can only answer mathematical questions.'"        
# EXAMPLE_QUESTION = "What is 2+2 ?"
# EXAMPLE_ANSWER = "four"
# response = client.chat.completions.create(
#     model="gpt-5-nano",
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": EXAMPLE_QUESTION},
#         {"role": "assistant", "content": EXAMPLE_ANSWER},
#         {"role": "user", "content": "12+34 ?"}
#     ],
# )

# print(response.choices[0].message.content)




#structured output with few shot prompting
# SYSTEM_PROMPT = "You are a helpful assistant. Who can answer only mathematical questions," \
#         " if user asks non mathematical question, " \
#         " you will respond with 'I can only answer mathematical questions.'"
# EXAMPLE_QUESTION = "What is 2+2 ?"
# EXAMPLE_ANSWER = "4:four"
# EXAMPLE_QUESTION_1 = "What is 3+5 ?"
# EXAMPLE_ANSWER_1 = "8:eight"
# response = client.chat.completions.create(
#     model="gpt-5-nano",
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": EXAMPLE_QUESTION},
#         {"role": "assistant", "content": EXAMPLE_ANSWER},
#         {"role":"user", "content": EXAMPLE_QUESTION_1},
#         {"role":"assistant", "content": EXAMPLE_ANSWER_1},
#         {"role": "user", "content": "12+34 ?"}
#     ],
# )     

# print(response.choices[0].message.content)



SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "You can answer only mathematical questions. "
    "If a non-mathematical question is asked, reply exactly with: "
    "'My master Bitan has asked not to reply on this. Please ask a mathematical question.' "
    "For mathematical questions, follow the format shown in the examples."
)

response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},

        {"role": "user", "content": "What is 2+2 ?"},
        {"role": "assistant", "content": "4:four:FOUR"},

        {"role": "user", "content": "What is 3+5 ?"},
        {"role": "assistant", "content": "8:eight:EIGHT"},

        {"role": "user", "content": "Who is modi ?"}
    ],
)

print(response.choices[0].message.content)