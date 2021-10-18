import unittest
import data


class DataAndKeys(unittest.TestCase):
    def test_compare_static_to_live(self):
        live = data.get_game_data(1)
        static = open("matches/1", "r").read()
        self.assertEqual(live, static)



if __name__ == '__main__':
    unittest.main()
