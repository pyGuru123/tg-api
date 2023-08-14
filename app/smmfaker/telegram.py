import random
import requests
from loguru import logger

async def make_request(order_id, payload, MAX_RETRIES):
    if MAX_RETRIES > 0:
        endpoint = f"https://smmblak.com/order/380{order_id:03}"
        logger.info(endpoint)

        response = requests.request("POST", endpoint, data=payload)
        if response.text.strip().startswith("<!DOCTYPE html>"):
            return "success"
            
        return response.text.strip()

    return "failed"

async def get_tg_views(post_url: str, views: int):
    MAX_RETRIES = 10

    order_id = random.randint(50, 100)
    payload = {
        'categories': ' 315',
        'services': ' 3060',
        'link': post_url,
        'quantity': views
    }

    response = await make_request(order_id, payload, MAX_RETRIES)
    if response != "success":
        make_request(order_id+1, payload, MAX_RETRIES-1)

    return "success"
