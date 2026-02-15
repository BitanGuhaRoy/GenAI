from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

client = Client(host="http://127.0.0.1:11434")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat(message: str = Body(..., description="The message")):
    response = client.chat(
        model="gemma2:2b",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return {"response": response.message.content}
