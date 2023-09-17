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
PALM_TOKEN = os.environ.get("PALM_TOKEN")
GPT_ENDPOINT = os.environ.get("GPT_ENDPOINT")

async def ask_bai(prompt: str):
    req_rand = random.randint(100000, 999999)
    url = f"https://beta.theb.ai/api/conversation?org_id={BAI_ORG_ID}&req_rand=0.397137{req_rand}"

    payload = json.dumps({
        "text": prompt,
        "category": "5be3c43f8bc740b792cce30cebdd861c",
        "model": "12cf0aaece3f4c27846aeb9c852dc0f9",
        "model_params": {},
        "topic_id": None,
        "stream": False
    })

    headers = {
        'Authorization': f'Bearer {BAI_TOKEN}',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text
    data = data.split("event: ")
    response = data[-2].strip().replace('{"content": "', "").split('"}')[0].replace('update\r\ndata: ', "")
    return response.strip().strip('"')


async def ask_llama(prompt: str):
    payload = json.dumps({
      "prompt": prompt,
      "version": "2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
      "systemPrompt": "You are a helpful assistant.",
      "temperature": 0.75,
      "topP": 0.9,
      "maxTokens": 800
    })

    headers = {
      "Content-Type": "application/json"
    }

    response = requests.post("https://www.llama2.ai/api", data=payload, headers=headers)
    return response.text


async def ask_palm(prompt: str):
    headers = {
        'Content-Type': 'application/json',
    }

    params = {
        'key': PALM_TOKEN,
    }

    json_data = {
        'prompt': {
            "messages": [{"content":prompt}]
        },
    }

    response = requests.post(
        'https://generativelanguage.googleapis.com/v1beta2/models/chat-bison-001:generateMessage',
        params=params,
        headers=headers,
        json=json_data,
    )

    return response.json()["candidates"][0]["content"]


async def ask_gpt(prompt: str, context: str):
    if not context:
        context ="You are ChatGPT, a large language model trained by OpenAI.\
                Carefully heed the user's instructions.\
                Respond using Markdown."

    payload = json.dumps({
      "messages": [
        {
          "role": "system",
          "content": context
        },
        {
          "role": "user",
          "content": prompt
        }
      ],
      "model": "gpt-3.5-turbo",
      "temperature": 1,
      "presence_penalty": 0,
      "top_p": 1,
      "frequency_penalty": 0,
      "stream": False
    })

    headers = {
      'Authorization': 'Bearer pk-this-is-a-real-free-pool-token-for-everyone',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", GPT_ENDPOINT, headers=headers, data=payload)
    return response.json()["choices"][0]["message"]["content"]