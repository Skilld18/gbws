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


def get_hero_together(hero, game):
    radiant_win = 0
    dire_win = 0
    if get_winner(game) == Side.RADIANT:
        radiant_win = 1
    elif get_winner(game) == Side.DIRE:
        dire_win = 1
    else:
        print("The goblins won")

    expected_together = dict()
    if hero in get_radiant_heroes(game):
        compatriots = get_radiant_heroes(game)
        compatriots.remove(hero)
        for c in compatriots:
            expected_together[frozenset({hero, c})] = radiant_win

    if hero in get_dire_heroes(game):
        compatriots = get_dire_heroes(game)
        compatriots.remove(hero)
        for c in compatriots:
            expected_together[frozenset({hero, c})] = dire_win


    return expected_together
