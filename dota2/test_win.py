import unittest
from test_const import *
from data import *


class WinTestCase(unittest.TestCase):
    def test_goblin_win(self):
        game = convert_data(get_static_game())
        self.assertEqual(get_winner(game), Side.GOBLINS)

    def test_dire_win(self):
        game = convert_data(get_game_data(known_good_match_id))
        self.assertEqual(get_winner(game), Side.DIRE)

    def test_radiant_win(self):
        game = convert_data(get_game_data(known_radiant_win))
        self.assertEqual(get_winner(game), Side.RADIANT)


if __name__ == '__main__':
    unittest.main()
