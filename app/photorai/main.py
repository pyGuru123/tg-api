import os
import io
import json
import base64
import random
import string
import platform
import requests
from loguru import logger

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

async def restore_picture(filename, content, withScratch=False):
    endpoint = "https://api.hotpot.ai/restore-picture"
    alphabet = random.choice(string.ascii_uppercase)
    payload = {
        'requestId': f'TK3uuTr0ogEU8P{alphabet}',
        'withScratch': withScratch
    }

    files=[
         ('image',(filename, content,'image/jpeg'))
    ]

    headers = {
         'Authorization': token
    }

    response = requests.request("POST", endpoint, headers=headers, data=payload, files=files)
    return response.content

async def remove_background(content):
    base64_image = base64.b64encode(content).decode('utf-8')

    payload = json.dumps({
        'image': "data:image/PNG;base64," + base64_image,
    })

    headers = {
      'Content-Type': 'application/json'
    }

    endpoint = "https://backend.zyro.com/v1/ai/remove-background"
    response = requests.request("POST", endpoint, data=payload, headers=headers)
    b64_string = response.json()['result']
    encoded_string = b64_string.strip().split(",")[1]
    b64_bytes = encoded_string.encode('utf-8')
    decoded_image = base64.decodebytes(b64_bytes)
    return decoded_image

async def upscale_image(content):
    base64_image = base64.b64encode(content).decode('utf-8')

    payload = json.dumps({
        'image_data': "data:image/PNG;base64," + base64_image,
    })

    headers = {
      'Content-Type': 'application/json'
    }

    endpoint = "https://upscaler.zyro.com/v1/ai/image-upscaler"
    response = requests.request("POST", endpoint, data=payload, headers=headers)
    try:
        b64_string = response.json()['upscaled']
        encoded_string = b64_string.strip().split(",")[1]
        b64_bytes = encoded_string.encode('utf-8')
        decoded_image = base64.decodebytes(b64_bytes)
        return decoded_image
    except:
        raise Exception(response.json()["message"])
