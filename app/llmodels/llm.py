import os
import json
import random
import requests
import platform
from loguru import logger

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

CHIMERA_ENDPOINT = os.environ.get("CHIMERA_ENDPOINT")
CHIMERA_TOKEN = os.environ.get("CHIMERA_TOKEN")
BAI_ORG_ID = os.environ.get("BAI_ORG_ID")
BAI_TOKEN = os.environ.get("BAI_TOKEN")

async def ask_bai(prompt: str):
    req_rand = random.randint(100000, 999999)
    url = f"https://beta.theb.ai/api/conversation?org_id={BAI_ORG_ID}&req_rand=0.397137{req_rand}"

    payload = json.dumps({
        "text": prompt,
        "category": "5be3c43f8bc740b792cce30cebdd861c",
        "model": "12cf0aaece3f4c27846aeb9c852dc0f9",
        "model_params": {},
        "topic_id": None
    })

    headers = {
        'Authorization': f'Bearer {BAI_TOKEN}',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text
    data = data.split("event: ")
    response = data[-2].strip().split("content")[-1].split(":")[1].strip('"}')
    return response.strip().strip('"')
    

async def ask_gpt(prompt: str):
    payload = {
      "model": "gpt-3.5-turbo-16k",
      "max_tokens": 2000,
      "messages": [
        {"role": "user", "content": prompt}
      ]
    }

    headers = {
      "Authorization": "Bearer " + CHIMERA_TOKEN,
      "Content-Type": "application/json"
    }

    response = requests.post(CHIMERA_ENDPOINT, json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"]


async def ask_llama(prompt: str):
    payload = {
      "model": "llama-2-70b-chat",
      "max_tokens": 2000,
      "messages": [
        {"role": "user", "content": prompt}
      ]
    }

    headers = {
      "Authorization": "Bearer " + CHIMERA_TOKEN,
      "Content-Type": "application/json"
    }

    response = requests.post(CHIMERA_ENDPOINT, json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"]