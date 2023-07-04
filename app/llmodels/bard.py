import os
import platform
import requests
from loguru import logger
from bardapi import Bard

if platform.system() == "Windows":
    from dotenv import load_dotenv
    load_dotenv()

token = os.environ.get("BARD_TOKEN")
session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", token)

bard = Bard(token=token, session=session, timeout=30)

async def ask_bard(prompt: str):
	result = bard.get_answer(prompt)
	return result['content']