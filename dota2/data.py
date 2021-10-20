import requests
from enum import Enum

import json
from collections import namedtuple


def custom_json_decoder(data):
    return namedtuple('Game', data.keys())(*data.values())


def get_game_data(game_id):
    return get_data("matches", game_id)


def get_hero_data(hero_id):
    return get_data("heroes", "")


def get_data(rest_api, key):
    api_url = "https://api.opendota.com/api/"
    return str(requests.get(api_url + rest_api + "/" +
                            str(key)).content.decode("utf-8"))


def get_key():
    with open("key", "r") as key:
        key_string = key.read().strip()
    return key_string


def convert_data(game):
    return json.loads(game, object_hook=custom_json_decoder)


class Side(Enum):
    GOBLINS = -1
    DIRE = 0
    RADIANT = 1


def get_winner(game):
    if game.radiant_win is True:
        return Side.RADIANT
    if game.radiant_win is False:
        return Side.DIRE
    return Side.GOBLINS
