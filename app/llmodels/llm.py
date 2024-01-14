import os
import json
import random
import requests
import platform
from loguru import logger

if platform.system() == "Windows":
    from dotenv import load_dotenv
    load_dotenv()

GPT4_ENDPOINT = "https://chat.gpt.bz/api/openai/v1/chat/completions?conversation_id=qao5oNacJChB9DRNbbTT-"
GEMINI_TOKEN = os.environ.get("GEMINI_TOKEN")
GPT4_TOKEN = os.environ.get("GPT4_TOKEN")

async def ask_llama(prompt: str):
    payload = json.dumps({
        "prompt": f"<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\n{prompt}[/INST]\n",
        "model": "meta/llama-2-70b-chat",
        "systemPrompt": "You are a helpful assistant.",
        "temperature": 0.75,
        "topP": 0.9,
        "maxTokens": 800,
        "image": None,
        "audio": None
    })

    headers = {
      "Content-Type": "application/json"
    }

    response = requests.post("https://www.llama2.ai/api", data=payload, headers=headers)
    return response.text


async def ask_gemini(prompt: str):
    headers = {
      'Content-Type': 'application/json'
    }

    payload = json.dumps({
      "contents": [
        {
          "parts": [
            {
              "text": prompt
            }
          ]
        }
      ]
    })

    response = requests.post(
        f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_TOKEN}',
        headers=headers,
        data=payload,
    )

    logger.info(response.json())
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]


async def ask_gpt4(prompt: str, context: str):
    if not context:
        context ="You are ChatGPT, a large language model trained by OpenAI.\
        Knowledge cutoff: 2021-09\
        Current model: gpt-4\
        Current time: 20/09/2023, 23:40:21"

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
            "stream": False,
            "model": "gpt-4"
        })

    headers = {
      'Authorization': GPT4_TOKEN,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", GPT4_ENDPOINT, headers=headers, data=payload)
    return response.json()["choices"][0]["message"]["content"]