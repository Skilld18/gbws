import requests
from game import *


def get_game_data(game_id):
    api_url = "https://api.opendota.com/api/"
    return str(requests.get(api_url + "matches/" +
                            str(game_id)).content.decode("utf-8"))


def get_key():
    return open("key", "r").read()


def convert_data(game):
    obj = Game()
    return obj
