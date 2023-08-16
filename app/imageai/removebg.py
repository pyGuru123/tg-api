import json
import base64
import requests
from loguru import logger

async def remove_background(content):
    endpoint = "https://backend.zyro.com/v1/ai/remove-background"
    base64_image = base64.b64encode(content).decode('utf-8')

    payload = json.dumps({
        'image': "data:image/png;base64," + base64_image,
    })

    logger.info(payload[:300])

    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", endpoint, data=payload, headers=headers)
    b64_string = response.json()['result']
    b64_string = b64_string + '=' * (4 - len(b64_string) % 4)
    decoded_binary_data = base64.b64decode(b64_string)
    with open('restored_image.jpg', 'wb') as image_file:
        image_file.write(decoded_binary_data)

    return "hahaha"