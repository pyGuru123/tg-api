import os
import time
import platform
import requests
from loguru import logger

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

TOKEN= os.environ.get("VYRO_TOKEN")

UNSTABLE_MODELS = {
    "digital": ["digital-art","digital-art"],
    "generalist": ["generalist", "generalist"],
    "anime": ["anime", "anime-base"],
    "photo": ["realistic", "realistic-photo"]
}

def get_unstable_model(model):
    if not model:
        return UNSTABLE_MODELS["digital"]

    return UNSTABLE_MODELS.get(model, ["digital-art","digital-art"])

async def unstable_all_models():
    return list(UNSTABLE_MODELS.keys())

def is_success(response: dict):
    return "<?xml" not in response.text


async def poll_image(url, success_condition, step=3, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = requests.get(url)
        if success_condition(response):
            return response
        time.sleep(step)
    raise TimeoutError("API request did not succeed within timeout")


async def unstable_diffusion(prompt: str, model: str="", secret_key: str=""):
    genre, style = get_unstable_model(model)
    logger.info(f"{genre=}, {style=}")

    url = "https://api.vyro.ai/v1/imagine/web/generations"
    data = {
                'model_version': 1
                'steps': 30
                'seed': 833108
                'cfg': 7.5
                'aspect_ratio': 1:1
                'prompt': prompt
                'negative_prompt': 
                'style_id': style_id
        }

    response = requests.post(url, data=data)
    data = response.json()
    image_id = data.get("id", None).strip("REQUEST#")
    if image_id:
        url = f"https://unstable-web-images.s3.amazonaws.com/{image_id}/0-original.png"
        response = await poll_image(url, is_success)
        return response.content
    else:
        raise Exception("No credits left")