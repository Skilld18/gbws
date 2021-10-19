import requests
from game import *


def get_game_data(game_id):
    api_url = "https://api.opendota.com/api/"
    return str(requests.get(api_url + "matches/" +
                            str(game_id)).content.decode("utf-8"))


def get_key():
    key = open("key", "r")
    key_string = key.read().strip()
    key.close()
    return key_string


def convert_data(game):
    obj = Game()
    return obj
