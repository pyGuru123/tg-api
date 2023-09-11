import requests
from loguru import logger
from bs4 import BeautifulSoup

async def get_cinevood_links(movie):
    movie_name = movie.replace(' ', '+')
    url = f"https://cinevood.co.uk/?s={movie_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find("article", class_="first")
    url = div.find("a")['href']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div", class_="download-btns")

    results = []
    for div in divs:
        try:
            result = {
                "name": div.find('h6').text,
                "link": div.find('a')['href']
            }
            results.append(result)
        except Exception as e:
            logger.error(f"{e=}")

    logger.info(results)
    return results