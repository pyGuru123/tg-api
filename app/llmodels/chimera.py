import os
import requests
import platform
from loguru import logger

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

CHIMERA_ENDPOINT = os.environ.get("CHIMERA_ENDPOINT")
CHIMERA_TOKEN = os.environ.get("CHIMERA_TOKEN")

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