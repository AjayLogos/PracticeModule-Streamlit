#%%
import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from prompts import solution_prompt , hints_prompt
from langchain_core.messages import HumanMessage, SystemMessage
from token_gen import get_user_token

# Function to extract base64 images from text
def extract_base64_images(text):
    pattern = r"(data:image\/(?:png|jpeg|jpg);base64,[a-zA-Z0-9+/=]+)"
    return re.findall(pattern, text)  # Returns a list of base64 image URLs

# Function to clean and extract meaningful text from HTML content
def clean_html(text):
    soup = BeautifulSoup(text, "html.parser")
    
    # Remove empty <figure> tags or any images inside them
    for figure in soup.find_all("figure"):
        if not figure.get_text(strip=True):  # Check if figure has meaningful text
            figure.decompose()  # Remove it completely

    # Extract meaningful text after removing figures & images
    cleaned_text = soup.get_text(separator=" ", strip=True)

    return cleaned_text

# Function to create a structured message
def create_message(question, solution, grade):
    message_content = []
    
    # Add grade level
    message_content.append({"type": "text", "text": f"GRADE: {grade}"})
    
    # Process question
    question_images = extract_base64_images(question)
    question_text = clean_html(re.sub(r"data:image\/(?:png|jpeg|jpg);base64,[a-zA-Z0-9+/=]+", "", question)).strip()

    if question_text:
        message_content.append({"type": "text", "text": f"QUESTION: {question_text}"})
    
    if question_images:
        message_content.append({"type": "text", "text": "QUESTION IMAGE:"})  # Label before images
        for img in question_images:
            message_content.append({"type": "image_url", "image_url": {"url": img}})

    # Process solution
    solution_images = extract_base64_images(solution)
    solution_text = clean_html(re.sub(r"data:image\/(?:png|jpeg|jpg);base64,[a-zA-Z0-9+/=]+", "", solution)).strip()

    if solution_text:
        message_content.append({"type": "text", "text": f"SOLUTION: {solution_text}"})

    if solution_images:
        message_content.append({"type": "text", "text": "SOLUTION IMAGE:"})  # Label before images
        for img in solution_images:
            message_content.append({"type": "image_url", "image_url": {"url": img}})

    return message_content


def fetch_question_details(ids):
    token = get_user_token()
    url = "https://newqbapi.infinitylearn.com/questions/ids"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {"ids": ids}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}
    

def get_prompt(question_id):
    question_ids = [question_id]
    result = fetch_question_details(question_ids)
    try:
        question = result['data'][0]['question']['question_text']
        solution = result['data'][0]['question']['solution'][0]['data']
        grade = result['data'][0]['toc_mapping'].get('grade', []) or 10

    
        message = create_message(question, solution, grade)
        message = HumanMessage(
            content=message
        )
        solution_system = SystemMessage(content=solution_prompt())
        hints_system = SystemMessage(content=hints_prompt())

        return {"Question":question,"Solution":solution,"hints_prompt":[hints_system, message],"solution_prompt":[solution_system, message]}
    except:
        return result
    

