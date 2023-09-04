import asyncio
import aiohttp
import requests
import concurrent.futures
from loguru import logger
from bs4 import BeautifulSoup

def scrape_results(soup):
    results = []

    table = soup.find("table", class_="c")
    rows = table.find_all("tr")
    for row in rows[1:]:
        text = row.text
        if "pdf" in text:
            atags = row.find_all("a")
            for atag in atags:
                href = atag["href"]
                if href.startswith("http://library.lol/"):
                    result = {
                        "name": text.split("\n")[2],
                        "size": text.split("\n")[-5],
                        "link": href
                    }
                    results.append(result)

    return results

def get_download_link(result):
    url = result['link']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find("div", id="download")
    if div:
        link = div.find("h2").find("a")["href"]
        result["link"] = link
        return result

async def scrape_libgen(isbn: str):
    url = f"http://libgen.rs/search.php?req={isbn}&open=0&res=25&view=simple&phrase=1&column=def"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    results = scrape_results(soup)
    responses = []

    if results:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            responses = list(executor.map(get_download_link, results))
        # async with aiohttp.ClientSession() as session:
        #     tasks = [get_download_link(session, result) for result in results]
        #     responses = await asyncio.gather(*tasks)
            responses = list(filter(lambda x : x is not None, responses))
    
    return responses