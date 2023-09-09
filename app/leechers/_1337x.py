import requests
import concurrent.futures
from loguru import logger
from bs4 import BeautifulSoup

def get_magnet(result):
    url = result["url"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    magnet = soup.find("a", class_="torrentdown2")
    if magnet:
        result["magnet"] = magnet["href"]
        del result["url"]
        return result

    return ""


async def get_1337x_magnet(movie):
    movie_name = movie.replace(" ", "%20")
    url = f"https://www.1377x.to/search/{movie_name}/1/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="table-list")
    body = table.find("tbody")
    rows = body.find_all("tr")
    results = []
    for row in rows:
        name = row.find("td", class_="name")
        url = "https://www.1377x.to" + name.find_all("a")[1]["href"]
        seeders = row.find("td", class_="seeds")
        leechers = row.find("td", class_="leeches")
        size = row.find("td", class_="size")
        result = {
            "name": name.text.strip(),
            "size": size.text,
            "seeders": seeders.text,
            "leechers": leechers.text,
            "url": url
        }

        results.append(result)

    responses = []
    if results:
        results = list(filter(lambda dct: "url" in dct.keys(), results))
        with concurrent.futures.ThreadPoolExecutor() as executor:
            responses = list(executor.map(get_magnet, results[:15]))

    return responses