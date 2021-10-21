import data


def get_public_matches():
    return data.convert_data(data.get_data("publicMatches", ""))


def get_public_ids():
    match_ids = []
    for match in get_public_matches():
        match_ids.append(match.match_id)
    return match_ids


def get_games():
    ids = get_public_ids()
    games = []
    for i in ids:
        try:
            games.append(data.convert_data(data.get_game_data(i)))
        except:
            print(id)
            print("Well that didn't work")
    return games
