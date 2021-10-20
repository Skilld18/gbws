known_good_match_id = 234523234


def get_static_game():
    match = open("matches/1", "r")
    match_str = match.read()
    match.close()
    return match_str
