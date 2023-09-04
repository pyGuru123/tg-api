import requests
from loguru import logger
from bs4 import BeautifulSoup

async def get_nyaasi_magnet(movie):
    movie_name = movie.replace(" ", "+")
    url = f"https://nyaa.si/?q={movie_name}&f=0&c=0_0"
    logger.info(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="torrent-list")
    if table:
        table_body = table.find("tbody")
        rows = table_body.find_all("tr")
        result_set = []

        for row in rows:
            cols = row.find_all("td")
            result = {
                "name": cols[1].text.strip().replace("\n", " - "),
                "size": cols[3].text.strip(),
                "magnet": cols[2].find_all("a")[1]['href']
            }

            result_set.append(result)

    return result_set