import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set. Please set it in your .env file.")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role = "user"

class Ticket(BaseModel):
    name: str
    issue: str
    email: str
    phone: int

schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}
system_prompt = f'''Extract the personal information from the customer ticket and return it in the following JSON format: {schema}. and give me json output only, do not give any other text.'''

system_message = {
    "role": "system",
    "content": system_prompt
}

text = "Hi, my name is Pradeep, I'm having issue with Iphone17 charger. I bought it from Amazom now its not charging, my mail id is pradeep@example.com and my phone number is +1-123-456-7890. Please help me to resolve this issue."
prompt = f'''This is customer ticket, please extract the personal infromation from this {text}'''
message = {
    "role": role,
    "content": prompt
}

messages = [system_message,message]
response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)
print(response.choices[0].message.content)