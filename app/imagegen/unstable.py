import os
import time
import platform
import requests
from loguru import logger

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

token = os.environ.get("UNSTABLE")
SECRET_KEY = os.environ.get("SECRET_KEY")

def is_success(response: dict):
    return "<?xml" not in response.text


async def poll_image(url, success_condition, step=3, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = requests.get(url)
        if success_condition(response):
            return response
        time.sleep(step)
    raise TimeoutError("API request did not succeed within timeout")


async def unstable_diffusion(prompt: str, model: str, secret_key: str):
    if secret_key != SECRET_KEY:
        raise Exception("You are unauthorised for this endpoint. Contact Author")

    url = "https://www.unstability.ai/api/submitPrompt"
    json = {
        "admin": False,
        "fingerprint": token,
        "genre": "digital-art",
        "style": "digital-art",
        "prompt": prompt,
        "negative_prompt": "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, blurred, watermark, grainy, signature, cut off, draft",
        "aspect_ratio": "1:1",
        "width": 640,
        "height": 640,
        "count": 1,
        "lighting_filter": "chaotic-composition",
        "lighting_filter_strength": 20,
        "lighting_filter_color": "#242424",
        "lighting_filter_negative_color": "#ebebeb",
        "alternate_mode": False,
        "detail_pass_strength": 50,
        "saturation": 60,
        "fast": False
    }
    cookies = {'__Host-next-auth.csrf-token': 'c24d7c99e0fe7be95ab097bde4e1076dd8d57c33db005ce81928e6cc72d5792b%7Ccbb65a25d78b2e80bb58dae8be8a00d2160dff31588b20684410ef27974a59dd',
               '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.unstability.ai%2F',
               '__Secure-next-auth.session-token': '6784466b-33b2-40bd-933d-27807dbf74ee'
              }

    response = requests.post(url, json=json, cookies=cookies)
    data = response.json()
    image_id = data.get("id", None).strip("REQUEST#")
    if image_id:
        url = f"https://unstable-web-images.s3.amazonaws.com/{image_id}/0-original.png"
        response = await poll_image(url, is_success)
        return response.content
    else:
        raise Exception("No credits left")