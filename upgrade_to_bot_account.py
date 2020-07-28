import requests
headers = {"Authorization": "Bearer TOKEN"}
r = requests.post("https://lichess.org/api/bot/account/upgrade", headers = headers)
