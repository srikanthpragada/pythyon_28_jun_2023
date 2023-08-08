from bs4 import BeautifulSoup
import requests

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
soup = BeautifulSoup(resp.text, 'html.parser')

for img in soup.find_all("img"):
    url = WEBSITE + "/" + img['src']
    print(url)






