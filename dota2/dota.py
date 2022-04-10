import requests
import json

api_key = ""
url = "https://api.opendota.com/api/matches/"
match = str(6486190411)
url += match + "?api_key=" + api_key

resp = requests.get(url=url)
data = resp.json() 
print(json.dumps(data, indent=4, sort_keys=True))
