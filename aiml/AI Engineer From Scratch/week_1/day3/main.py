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

prompt1 = "Hi!"
prompt2 = "What is time travel in detail?"
prompt3 = "Write 300 words essay on the topic 'The impact of AI on society'."

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
    "role": role,
    "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=100)
    usage = response.usage
    print(f"Prompt: {prompt}, Your Token --> {usage.prompt_tokens}, Completion Token --> {usage.completion_tokens}, Total Token --> {usage.total_tokens}, Finish Reason --> {response.choices[0].finish_reason}")