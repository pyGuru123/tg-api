import time
import requests
from app.imagegen.models import (
    get_model,
    all_models,
    get_model_tensor
)

def is_success(response: dict):
  return response.json()["status"] == "succeeded"

async def poll_api(url, success_condition, step=1, timeout=20):
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = requests.get(url)
        if success_condition(response):
            return True
        time.sleep(step)
    raise TimeoutError("API request did not succeed within timeout")

async def imagine(prompt: str, model: str) -> bytes:
    negatives = "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs,\
             disfigured, deformed, body out of frame, blurry, bad anatomy, blurred, watermark, grainy,\
              signature, cut off, draft".replace(",", "%2C").replace(" ", "+")
    try:
        prompt = "+".join(prompt.split(" "))
        model = get_model_tensor(model)
        endpoint = f"https://api.prodia.com/generate?new=true&prompt={prompt}&model={model}&\
                    negative_prompt={negatives}&steps=25&cfg=7&seed=2280986900&sampler=DPM%2B%2B+2M+Karras&aspect_ratio=square"
        response = requests.get(endpoint)
        job_id = response.json()["job"]

        url = f"https://api.prodia.com/job/{job_id}"
        response = await poll_api(url, is_success)
        if response:
            url = f"https://images.prodia.xyz/{job_id}.png?download=1"
            response = requests.get(url)
            return response.content
    except Exception as e:
        return str(e)