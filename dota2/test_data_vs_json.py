import unittest
import data

known_good_match_id = 234523234


def get_static_game():
    match = open("matches/1", "r")
    match_str = match.read()
    match.close()
    return match_str


class DataAndKeys(unittest.TestCase):

    def test_compare_static_to_live(self):
        live = data.get_game_data(1)
        self.assertEqual(live, get_static_game())

    def test_convert_data(self):
        static_game = data.convert_data(get_static_game())
        live_game = data.convert_data(data.get_game_data(known_good_match_id))
        self.assertEqual(str(type(static_game)), str(type(live_game)))

    def test_game_match_id(self):
        game = data.convert_data(get_static_game())
        self.assertEqual(game.match_id, 1)

    def test_game_match_id_add(self):
        game = data.convert_data(data.get_game_data(3))
        self.assertEqual(game.match_id, 3)


if __name__ == '__main__':
    unittest.main()
