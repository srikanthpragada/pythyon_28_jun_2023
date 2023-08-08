from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
soup = BeautifulSoup(resp.text, 'html.parser')

for img in soup.find_all("img"):
    url = img['src']
    if not url.startswith("/"):
        url = "/" + url

    print(WEBSITE + url)
