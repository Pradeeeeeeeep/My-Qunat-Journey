import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from groq import Groq
from pypdf import PdfReader

reader = PdfReader("Pradeep_CV.pdf")

pdf_content = []
for page in reader.pages:
    pdf_content.append(page.extract_text())

full_text = "\n".join(pdf_content)

load_dotenv(find_dotenv("../.env"))
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set. Please set it in your .env file.")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
prompt = f"check this resume and give me a summary of the candidate's skills, experience, and qualifications. Please provide the summary in a table format in which role I should hire him.\n\n{full_text}"
message = {
    "role": role,
    "content": prompt
}

messages = [message]
response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)