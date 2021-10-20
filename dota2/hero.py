from data import *


def get_hero_name(hero_id):
    data = get_hero_data(hero_id)
    data = convert_data(data)
    for hero in data:
        if hero.id == hero_id:
            return hero.localized_name


def get_heroes(game, is_radiant):
    heroes = set()
    for player in game.players:
        if player.isRadiant == is_radiant:
            heroes.add(get_hero_name(player.hero_id))
    return heroes


def get_radiant_heroes(game):
    return get_heroes(game, True)


def get_dire_heroes(game):
    return get_heroes(game, False)
