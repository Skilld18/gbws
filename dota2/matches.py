import data
import hero


def get_public_matches():
    return data.convert_data(data.get_data("publicMatches", ""))


def radiant_win(game):
    return game.radiant_win


def get_heroes(team):
    return set(map(lambda x: hero.get_hero_name(int(x)), team.split(',')))


def get_radiant_heroes_public(game):
    return get_heroes(game.radiant_team)


def get_dire_heroes_public(game):
    return get_heroes(game.dire_team)
