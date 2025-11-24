from google import genai 
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel
from pprint import pprint
import os 
import sys

class Page(BaseModel):
    category: str # Category:{topic}


client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')


try:
    with open('prompt_instructions.txt','r') as f:
        prompt_instructions=f.read() 
except:
    print('Missing System Instruction, check file path ')
    sys.exit()


question = input("Enter your intrest > ")
response = chat.send_message(
    question,
    config=GenerateContentConfig(
        system_instruction=prompt_instructions,
        response_mime_type='application/json',
        response_schema=Page
    )
)
temppage = response.parsed
print(temppage.category)

