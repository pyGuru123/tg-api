import os
import pytz
import platform
import requests
from loguru import logger
from datetime import datetime

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

api_token = os.environ.get("NASA_TOKEN")
indian_tz = pytz.timezone('Asia/Kolkata')

def todays_date():
    today = datetime.now(indian_tz)
    return today.strftime("%Y-%m-%d")

async def astronomy_pic_of_day(date):
	url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={api_token}"
	response = requests.get(url)
	return response.json()