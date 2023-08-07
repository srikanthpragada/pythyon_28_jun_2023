import requests

resp = requests.get("https://api.github.com/users/gvanrossum12345")

if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()


details = resp.json()

print(details["name"])
print(details["company"])
print(details["location"])