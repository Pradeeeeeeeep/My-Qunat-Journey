import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set. Please set it in your .env file.")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
prompt = "Give me a name for a new restaurant that serves Indian food, name should be one word"
sys_message = {
    "role": "system",
    "content": "You are a brand manager who suggests brand names for new products. You are creative and witty, and you always provide a list of 5 brand name suggestions."
}
message = {
    "role": role,
    "content": prompt
}

messages = [sys_message, message]
response = client.chat.completions.create(model=model, messages=messages, temperature=2)
print(response.choices[0].message.content)