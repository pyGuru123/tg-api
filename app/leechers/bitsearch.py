import requests
from loguru import logger
from bs4 import BeautifulSoup


async def get_bitsearch_magnet(movie):
    movie_name = movie.replace(" ", "+")
    url = f"https://bitsearch.to/search?q={movie_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("li", class_="search-result")
    results = []
    for row in rows:
        name = row.find("h5", class_="title").text.strip()
        stats_div = row.find("div", class_="stats")
        stats_divs = stats_div.find_all("div")
        size = stats_divs[1].text.strip()
        magnet = row.find("a", class_="dl-magnet")['href']

        result = {
            "name": name,
            "size": size,
            "magnet": magnet
        }

        results.append(result)

    return results