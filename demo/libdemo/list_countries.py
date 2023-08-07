import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for c in countries:
    capital = c.get('capital', ['Unknown'])
    print(f"{c['name']['common']:40}  {capital[0]:20}   {c['population']:10}")

