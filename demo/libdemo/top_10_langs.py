from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.tiobe.com/tiobe-index/"
resp = requests.get(WEBSITE)
soup = BeautifulSoup(resp.text, 'html.parser')

table = soup.find(id="top20")
body = table.tbody
rows = body.find_all("tr")
for row in rows[:10]:
    cols = row.find_all("td")
    print(f"{cols[4].text:20}  {cols[5].text:10}")
