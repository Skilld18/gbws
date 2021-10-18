import unittest
import data
import game as g

known_good_match_id = 234523234


def get_static_game():
    return open("matches/2", "r").read()


class DataAndKeys(unittest.TestCase):

    def test_compare_static_to_live(self):
        live = data.get_game_data(1)
        self.assertEqual(live, get_static_game())

    def test_convert_data(self):
        game = data.convert_data(get_static_game())
        self.assertEqual(type(game), type(g.Game()))

    def test_game_match_id(self):
        game = data.convert_data(get_static_game())
        self.assertEqual(game.match_id, 2)


if __name__ == '__main__':
    unittest.main()
