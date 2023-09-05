import requests
import concurrent.futures
from loguru import logger
from bs4 import BeautifulSoup

def get_magnet(result):
    url = "https://zooqle.xyz/torrent-page/"
    if result["id"]:
        form_data = {
            "id": result["id"]
        }

        response = requests.post(url, data=form_data)
        soup = BeautifulSoup(response.text, "html.parser")
        atags = soup.find_all("a", class_="download")
        magnet = None
        for tag in atags:
            if "magnet" in tag['href']:
                result["magnet"] = tag["href"]
                break

        del result["id"]
    return result


async def get_zooqle_magnet(movie):
    url = "https://zooqle.xyz/search/"
    form_data = {
        "q": movie
    }
    response = requests.post(url, data=form_data)
    soup = BeautifulSoup(response.text, "html.parser")
    logger.info(f"{soup.title}")

    table = soup.find("table", class_="film-table")
    table_body = table.find("tbody")
    rows = table_body.find_all("tr")
    results = []
    for row in rows:
        cols = row.find_all("td")
        name = cols[0].text.strip()
        id = cols[0].find("input").get('value')
        size = cols[1].text.strip()

        result = {
            "name": name,
            "id": id,
            "size": size
        }
        results.append(result)

    responses = []
    if results:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            responses = list(executor.map(get_magnet, results[:15]))

    return responses

