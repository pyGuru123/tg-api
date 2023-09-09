import requests
import concurrent.futures
from loguru import logger
from bs4 import BeautifulSoup

def get_magnet(result):
    url = result["url"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    magnet_div = soup.find("div", class_="downloadButtonGroup")
    magnet = magnet_div.find("a")
    if magnet:
        result["magnet"] = magnet["href"]
        del result["url"]
        return result

    return ""


async def get_kickass_magnet(movie):
    movie_name = movie.replace(" ", "%20")
    url = f"https://kickasstorrents.to/usearch/{movie_name}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="data")
    rows = table.find_all("tr")
    results = []
    for row in rows[1:]:
        cols = row.find_all("td")
        name = cols[0].text.split('TGx')[0].strip()
        link_div = row.find("div", class_="torrentname")
        url = "https://kickasstorrents.to/" + link_div.find("a")['href']
        size = cols[1].text.strip()
        seeders = cols[4].text.strip()
        leechers = cols[5].text.strip()

        result = {
            "name": name,
            "size": size,
            "seeders": seeders,
            "leechers": leechers,
            "url": url
        }

        results.append(result)

    responses = []
    if results:
        results = list(filter(lambda dct: "url" in dct.keys(), results))
        with concurrent.futures.ThreadPoolExecutor() as executor:
            responses = list(executor.map(get_magnet, results[:15]))

    return responses