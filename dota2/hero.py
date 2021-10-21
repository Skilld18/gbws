import data
from data import *


def get_hero_name(hero_id):
    data = get_hero_data()
    data = convert_data(data)
    for hero in data:
        if hero.id == hero_id:
            return hero.localized_name


def get_heroes(game, is_radiant):
    return {
        get_hero_name(player.hero_id)
        for player in game.players
        if player.isRadiant == is_radiant
    }


def get_radiant_heroes(game):
    return get_heroes(game, True)


def get_dire_heroes(game):
    return get_heroes(game, False)


def get_hero_together(hero, game, together):
    radiant_win = 0
    dire_win = 0
    if get_winner(game) == Side.RADIANT:
        radiant_win = 1
    elif get_winner(game) == Side.DIRE:
        dire_win = 1
    else:
        print("The goblins won")
    if hero not in together:
        together[hero] = 0
    if hero in get_dire_heroes(game) or hero in get_radiant_heroes(game):
        together[hero] += 1

    if hero in get_radiant_heroes(game):
        compatriots = get_radiant_heroes(game)
        compatriots.remove(hero)
        for c in compatriots:
            if frozenset({hero, c}) not in together:
                together[frozenset({hero, c})] = 0
            together[frozenset({hero, c})] += radiant_win
            if frozenset({hero, c, True}) not in together:
                together[frozenset({hero, c, True})] = 0
            together[frozenset({hero, c, True})] += 1


    if hero in get_dire_heroes(game):
        compatriots = get_dire_heroes(game)
        compatriots.remove(hero)
        for c in compatriots:
            if frozenset({hero, c}) not in together:
                together[frozenset({hero, c})] = 0
            together[frozenset({hero, c})] += dire_win
            if frozenset({hero, c, True}) not in together:
                together[frozenset({hero, c, True})] = 0
            together[frozenset({hero, c, True})] += 1


    return together


def get_game_count(hero, together):
    return together[hero]


def get_hero_list():
    hero_obj = convert_data(get_hero_data())
    heroes = []
    for hero in hero_obj:
        heroes.append(hero.localized_name)
    return heroes
