known_good_match_id = 234523234
known_radiant_win = 234523236
known_razor_game = known_radiant_win


def get_static_game():
    with open("matches/1", "r") as match:
        match_str = match.read()
    return match_str
