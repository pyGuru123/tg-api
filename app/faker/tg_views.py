import requests
import random
import sys
import threading
import psutil
import os
import asyncio
import aiohttp
from loguru import logger

def scrape_proxy(url):
    try:
        response = requests.get(url, allow_redirects=True)
        result = []
        for proxy in response.content.decode().replace("\r",'').split("\n"):
            result.append(proxy)
    except Exception as e:
        logger.error(f"{e=}")
    finally:
        return result


#=================================[PROXY]==========================================
def http(count):
    hits = []
    http_urls = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
        "https://www.proxyscan.io/download?type=http",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://www.proxyscan.io/download?type=http",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    ]

    for http_url in http_urls[:count]:
        proxies = scrape_proxy(http_url)
        hits.extend(proxies)

    hits = set(hits)
    hits = "\n".join(hits)
    return hits.split()

def socks4():
    hit = []

    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all", allow_redirects=True)
        r1 = requests.get("https://www.proxyscan.io/download?type=socks4", allow_redirects=True)
        r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4", allow_redirects=True)
        r3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt", allow_redirects=True)
        for x1 in r.content.decode().replace("\r",'').split("\n"):
            hit.append(x1)
        for x2 in r1.content.decode().replace("\r",'').split("\n"):
            hit.append(x2)
        for x3 in r2.content.decode().replace("\r",'').split("\n"):
            hit.append(x3)
        for x4 in r3.content.decode().replace("\r",'').split("\n"):
            hit.append(x4)
        
    except:
        r1 = requests.get("https://www.proxyscan.io/download?type=socks4", allow_redirects=True)
        r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4", allow_redirects=True)
        r3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt", allow_redirects=True)
        for x2 in r1.content.decode().replace("\r",'').split("\n"):
            hit.append(x2)
        for x3 in r2.content.decode().replace("\r",'').split("\n"):
            hit.append(x3)
        for x4 in r3.content.decode().replace("\r",'').split("\n"):
            hit.append(x4)
    hit = set(hit)
    hit = "\n".join(hit)
    return hit.split()

def socks5():
    hit = []
    try:
        zxcvv = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks5",timeout=8).json()["data"]
        for okeys in zxcvv:
            hit.append(okeys['ip']+":"+okeys['port'])
    except:
        pass

    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all", allow_redirects=True)
        r1 = requests.get("https://www.proxyscan.io/download?type=socks5", allow_redirects=True)
        r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5", allow_redirects=True)
        r3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", allow_redirects=True)
        for x1 in r.content.decode().replace("\r",'').split("\n"):
            hit.append(x1)
        for x2 in r1.content.decode().replace("\r",'').split("\n"):
            hit.append(x2)
        for x3 in r2.content.decode().replace("\r",'').split("\n"):
            hit.append(x3)
        for x4 in r3.content.decode().replace("\r",'').split("\n"):
            hit.append(x4)
        
    except:
        r1 = requests.get("https://www.proxyscan.io/download?type=socks5", allow_redirects=True)
        r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5", allow_redirects=True)
        r3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", allow_redirects=True)
        for x2 in r1.content.decode().replace("\r",'').split("\n"):
            hit.append(x2)
        for x3 in r2.content.decode().replace("\r",'').split("\n"):
            hit.append(x3)
        for x4 in r3.content.decode().replace("\r",'').split("\n"):
            hit.append(x4)
    hit = set(hit)
    hit = "\n".join(hit)
    return hit.split()

#=================================[DEF]==========================================

def socks4_start(link, proxy_4, count):
    global req_count
    req_count = 0

    while proxy_4 != []:
        if req_count >= int(count):
            p = psutil.Process(os.getpid())
            p.terminate()

        proxy = random.choice(proxy_4)

        try:
            session = requests.session()
            session.proxies.update({'http': f'socks4://{proxy}', 'https': f'socks4://{proxy}'})
            session.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
                })
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get("https://t.me/v/?views=" + _token)
            logger.info(f"Stats Code: {(views_req.status_code)} - View Count : {req_count+1}")
            proxy_4.remove(proxy)
            req_count += 1
        except:
            pass

def socks5_start(link):
    global proxy_5, count, req_count
    while proxy_5 != []:
        if req_count >= int(count):
            p = psutil.Process(os.getpid())
            p.terminate()
        proxy = random.choice(proxy_5)
        try:
            session = requests.session()
            session.proxies.update({'http': f'socks5://{proxy}', 'https': f'socks5://{proxy}'})
            session.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
                })
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get("https://t.me/v/?views=" + _token)
            print(' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code))
            proxy_5.remove(proxy)
            req_count += 1
        except:
            pass

# async def http_start(link, proxy_h, count):
#     global req_count

#     while proxy_h != []:
#         if req_count >= int(count):
#             p = psutil.Process(os.getpid())
#             p.terminate()

#         proxy = random.choice(proxy_h)
#         try:
#             session = requests.session()
#             session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
#             session.headers.update({
#                 'accept-language': 'en-US,en;q=0.9',
#                 'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
#                 'x-requested-with': 'XMLHttpRequest'
#                 })
            # main_res = session.get(link)
#             _token = main_res.text.split('data-view="')[1].split('"')[0]
#             views_req = session.get("https://t.me/v/?views=" + _token)
#             logger.info(f"Stats Code: {(views_req.status_code)} - View Count : {req_count+1}")
#             proxy_h.remove(proxy)
# #             req_count += 1
#         except:
#             pass

async def http_start(link, proxy_h, count):
    global req_count

    while proxy_h and req_count < int(count):
        proxy = random.choice(proxy_h)
        try:
            async with aiohttp.ClientSession(headers={
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
            }) as session:
                async with session.get(link, proxy=f"http://{proxy}") as main_res:
                    text = await main_res.text()
                    _token = text.split('data-view="')[1].split('"')[0]
                    async with session.get(f"https://t.me/v/?views={_token}") as views_req:
                        logger.info(f"Stats Code: {views_req.status} - View Count: {req_count+1}")
                        proxy_h.remove(proxy)
                        req_count += 1
                        logger.info(f"{count=} : {req_count=} {len(proxy_h)}")
                        if req_count > count:
                            break
        except:
            pass
        
        
# #=================================[START]==========================================

# def main(url, count, type="socks4", scrapers=2):
#     url_fin = f"{url}?embed=1"

#     if type=="socks4":
#         proxy_4 = socks4()
#         logger.info(f"fetched {len(proxy_4)} socks4 proxies")
#         for _ in range(600):
#             threading.Thread(target=socks4_start,args=(url_fin, proxy_4, count)).start()
#     elif type=="http":
#         http_proxies = http(scrapers)
#         logger.info(f"fetched {len(http_proxies)} socks4 proxies")
#         for _ in range(600):
#             threading.Thread(target=http_start,args=(url_fin, http_proxies, count)).start()

async def main(url, count, type="socks4", scrapers=2):
    url_fin = f"{url}?embed=1"
    global req_count
    req_count = 0

    if type=="socks4":
        proxy_4 = socks4()
        logger.info(f"scraped {len(proxy_4)} socks4 proxies")
        for _ in range(600):
            threading.Thread(target=socks4_start,args=(url_fin, proxy_4, count)).start()

    elif type=="http":
        http_proxies = http(scrapers)
        logger.info(f"scraped {len(http_proxies)} http proxies")
        tasks = []

        for _ in range(600):
            # threading.Thread(target=http_start,args=(url_fin, http_proxies, count)).start()
            task = asyncio.create_task(http_start(url_fin, http_proxies, count))
            tasks.append(task)

        await asyncio.gather(*tasks)

asyncio.run(main("https://t.me/sanatandhrma/90", 50, "http"))