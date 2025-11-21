from google import genai 
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel
from pprint import pprint
import os 
import sys

class Page(BaseModel):
    category: str 
    # title: str
    # link: str
    # summary: str


client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')


try:
    with open('prompt_instructions.txt','r') as f:
        prompt_instructions=f.read() 
except:
    print('Missing System Instruction, check file path ')
    sys.exit()

while True:
    question = input("Enter your intrest > ")
    response = chat.send_message(
        question,
        config=GenerateContentConfig(
            system_instruction=prompt_instructions,
            response_schema=Page
        )
    )
    temppage = response.parsed
    print(temppage.category)

# recipe = response.parsed  # Pydantic Recipe object 
# print(f'How to make {recipe.recipe_name}')  # Can use fields to access data 
# print('*** You will need these ingredients ***')
# for ingredient in recipe.ingredients:
#     print(ingredient)
# print('*** And here are the instructions ***')
# for step in recipe.instructions:
#     print(step)

# print()

# # Or, if you want dictionaries and lists 
# recipe_dictionary = response.parsed.model_dump()

# pprint(recipe_dictionary)
# print('*** You will need these ingredients ***')
# print(recipe_dictionary['recipe_name'])
# for ingredient in recipe_dictionary['ingredients']:
#     print(ingredient)
# print('*** And here are the instructions ***')
# for step in recipe_dictionary['instructions']:
#     print(step)