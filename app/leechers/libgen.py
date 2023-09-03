import asyncio
import aiohttp
import requests
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
                if href.startswith("http://library.lol/") or href.startswith("http://libgen.li/"):
                    result = {
                        "name": text.split("\n")[2],
                        "size": text.split("\n")[-5],
                        "link": href
                    }
                    results.append(result)

    return results

async def get_download_link(session, result):
    url = (result['link'])
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
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
        async with aiohttp.ClientSession() as session:
            tasks = [get_download_link(session, result) for result in results]
            responses = await asyncio.gather(*tasks)
            responses = list(filter(lambda x : x is not None, responses))
    
    return responses