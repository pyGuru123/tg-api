import requests
from bs4 import BeautifulSoup
from typing import Union

from app.model import nhentaiResponse

async def main(id: int) -> Union[nhentaiResponse, dict]:
    response = {}
    r = requests.get(f"https://nhentai.to/g/{id}/1")
    if r.status_code == 404:
        raise Exception("Page not found")

    soup = BeautifulSoup(r.text, "html.parser")
    total_pages = soup.find("span", class_="num-pages")
    images = soup.find_all("img")

    for img in images:
        src = img.get("src")
        if "https://cdn.dogehls" in src:
            response["cdn_url"] = src
            response["cdn_id"] = int(src.split("galleries/")[1].split("/")[0])
            response["num_pages"] = total_pages.text
            response["urls"] = [src.strip("1.jpg") + f"{page}.jpg" 
                                        for page in range(1, int(total_pages.text)+1)]

    return response