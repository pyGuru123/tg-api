import requests
from bs4 import BeautifulSoup


r = requests.get("https://betterprogramming.pub/101-funny-programmer-quotes-76c7f335b92d")
html = r.content
soup = BeautifulSoup(html, "html.parser")
lis = soup.findall("li", class_="ob oc")
for li in lis:
	print(li.text)