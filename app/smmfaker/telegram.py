import random
import requests
from loguru import logger

async def get_tg_views(post_url: str, views: int):
    order_id = random.randint(1000, 9999)
    endpoint = f"https://smmblak.com/order/38{order_id}"

    payload = {
        'categories': ' 315',
        'services': ' 3060',
        'link': post_url,
        'quantity': views
    }

    response = requests.request("POST", endpoint, data=payload)
    if response.text.startswith("<!DOCTYPE html>"):
        return "success"
        
    return "failed" 