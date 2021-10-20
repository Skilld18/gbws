from data import *


def get_hero_name(hero_id):
    data = get_hero_data(hero_id)
    data = convert_data(data)
    for hero in data:
        if hero.id == hero_id:
            return hero.localized_name


def get_radiant_heroes(game):
    heroes = set()
    for player in game.players:
        if player.isRadiant:
            heroes.add(get_hero_name(player.hero_id))
    return heroes

def get_dire_heroes():
    actual = set()
    actual.add("Jakiro")
    actual.add("Necrophos")
    actual.add("Lion")
    actual.add("Viper")
    actual.add("Dragon Knight")
    return actual