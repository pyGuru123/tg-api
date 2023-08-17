import json
import io
import base64
import requests
from loguru import logger

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