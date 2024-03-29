from data import *
import matches
from matches import radiant_win


def get_hero_name(hero_id):
    dat = get_hero_data()
    dat = convert_data(dat)
    for hero in dat:
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
    rad_win = 0
    dir_win = 0
    if get_winner(game) == Side.RADIANT:
        rad_win = 1
    elif get_winner(game) == Side.DIRE:
        dir_win = 1
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
            together[frozenset({hero, c})] += rad_win
            if frozenset({hero, c, True}) not in together:
                together[frozenset({hero, c, True})] = 0
            together[frozenset({hero, c, True})] += 1

    if hero in get_dire_heroes(game):
        compatriots = get_dire_heroes(game)
        compatriots.remove(hero)
        for c in compatriots:
            if frozenset({hero, c}) not in together:
                together[frozenset({hero, c})] = 0
            together[frozenset({hero, c})] += dir_win
            if frozenset({hero, c, True}) not in together:
                together[frozenset({hero, c, True})] = 0
            together[frozenset({hero, c, True})] += 1

    return together


def get_public_hero_together(hero, game, together):
    add = 0
    compatriots = set()
    if hero not in together:
        together[hero] = 0
    if hero in matches.get_radiant_heroes_public(game) or hero in matches.get_dire_heroes_public(game):
        together[hero] += 1
        if hero in matches.get_radiant_heroes_public(game):
            compatriots = matches.get_radiant_heroes_public(game)
            if radiant_win(game):
                add = 1
        else:
            compatriots = matches.get_dire_heroes_public(game)
            if not radiant_win(game):
                add = 1
        compatriots.remove(hero)

    for c in compatriots:
        if frozenset({hero, c}) not in together:
            together[frozenset({hero, c})] = 0
        together[frozenset({hero, c})] += add
        if frozenset({hero, c, True}) not in together:
            together[frozenset({hero, c, True})] = 0
        together[frozenset({hero, c, True})] += 1
    return together


def get_game_count(hero, together):
    return together[hero]


def get_hero_list():
    hero_obj = convert_data(get_hero_data())
    return [hero.localized_name for hero in hero_obj]
