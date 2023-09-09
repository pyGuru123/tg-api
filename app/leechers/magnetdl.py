import requests
import concurrent.futures
from loguru import logger
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)\
             Chrome/116.0.0.0 Mobile Safari/537.36"
headers = {'User-Agent': user_agent}

def get_magnet(result):
    url = "https://magnetdl.cfd/torrent-page/"
    if result["id"]:
        form_data = {
            "id": result["id"]
        }

        response = requests.post(url, data=form_data)
        soup = BeautifulSoup(response.text, "html.parser")
        atags = soup.find_all("a")
        magnet = None
        for tag in atags:
            if "magnet" in tag['href']:
                result["magnet"] = tag["href"]
                break

        del result["id"]
    return result

async def get_magnetdl_magnet(movie):
    url = "https://magnetdl.cfd/search-results/"
    form_data = {
        "category": "all",
        "q": movie
    }
    response = requests.post(url, data=form_data, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", id="content")
    table = content.find("table")

    rows = table.find_all("tr")
    results = []
    for row in rows:
        cols = row.find_all("td")
        if cols:
            name = cols[0].text.strip()
            seeders = cols[2].text
            leechers = cols[3].text
            size = cols[5].text
            id = cols[0].find("input").get('value')

            result = {
                "name": name,
                "size": size,
                "seeders": seeders,
                "leechers": leechers,
                "id": id,
            }
            results.append(result)

    responses = []
    if results:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            responses = list(executor.map(get_magnet, results[:15]))

    return responses