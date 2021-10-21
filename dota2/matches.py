import data


def get_public_matches():
    return data.convert_data(data.get_data("publicMatches", ""))


def radiant_win(game):
    return game.radiant_win
