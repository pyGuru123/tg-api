import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup

from app.model import sanatanResponse

def todays_date():
    today = datetime.today()
    return today.strftime("%d %B, %Y")

def process_text(text):
    text = re.sub(r"\s+", " ", text.strip())
    text = text.strip().replace("\xa0", " ")
    return text

async def gitapress_data() -> sanatanResponse:
    url = "https://www.gitapress.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    date = todays_date()

    suntime = soup.find_all("span", class_="suntime-content")
    shloka = soup.find("div", class_="cardshloka")
    importance = soup.find("span", class_="todays-importance-content")

    sunrise = process_text(suntime[0].text)
    sunset = process_text(suntime[1].text)
    shloka = process_text(shloka.text).replace("--", "\n--")
    importance = process_text(importance.text)

    shloka = shloka.strip("Shloka of The Day ")

    data_dict = {
        "message": "success",
        "error": "",
        "date": date,
        "sunrise": sunrise,
        "sunset": sunset,
        "shloka": shloka,
        "importance": importance
    }

    return data_dict