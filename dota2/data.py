import requests


def get_game_data():
    api_url = "https://api.opendota.com/api/"
    return str(requests.get(api_url + "matches/1").content)


def get_key():
    return open("key", "r").read()
