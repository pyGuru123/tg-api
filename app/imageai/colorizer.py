import os
import platform
import requests
import random
import string

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

token = os.environ.get("HOTPOT_KEY")

async def colorize_picture(filename, content):
    endpoint = "https://api.hotpot.ai/colorize-picture"
    alphabet = random.choice(string.ascii_uppercase)
    payload = {
      'requestId': f'TK3uuTr0ogEU8P{alphabet}',
      'renderFactor': '20'
    }

    files=[
    ('image',(filename, content,'image/jpeg'))
    ]

    headers = {
    'Authorization': token
    }

    response = requests.request("POST", endpoint, headers=headers, data=payload, files=files)
    return response.content

# async def restore_picture(filename, content, withScratch=False):
  