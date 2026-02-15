from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCXk_YWvX72MSqLc7myjRCaNQbsl0XKimk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "what do you know about india"
        }
    ]
)

print(response.choices[0].message)