import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for c in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    capital = c.get('capital', ['Unknown'])
    print(f"{c['name']['common']:40}  {c['population']:10} {c['area']:10}")
