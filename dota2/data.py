import requests

import json
from collections import namedtuple


def custom_json_decoder(data):
    return namedtuple('Game', data.keys())(*data.values())


def get_game_data(game_id):
    api_url = "https://api.opendota.com/api/"
    return str(requests.get(api_url + "matches/" +
                            str(game_id)).content.decode("utf-8"))


def get_key():
    with open("key", "r") as key:
        key_string = key.read().strip()
    return key_string


def convert_data(game):
    return json.loads(game, object_hook=custom_json_decoder)


def get_winner():
    pass
