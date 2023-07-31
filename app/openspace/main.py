import os
import pytz
import platform
import requests
from loguru import logger
from datetime import datetime, timedelta

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

api_token = os.environ.get("NASA_TOKEN")
indian_tz = pytz.timezone('Asia/Kolkata')

def todays_date(delta=0):
    today = datetime.now(indian_tz) - timedelta(days=delta)
    return today.strftime("%Y-%m-%d")

async def astronomy_pic_of_day(date):
	url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={api_token}"
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()

	data = response.json()
	if "Date must be between" in data["msg"]:
		url = f"https://api.nasa.gov/planetary/apod?date={todays_date(1)}&api_key={api_token}"
		response = requests.get(url)
		return response.json()

async def where_is_iss():
	url = "https://api.wheretheiss.at/v1/satellites/25544"
	response = requests.get(url)
	return response.json()