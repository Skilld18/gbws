import unittest
from matches import *
from test_const import *


class MatchTestCase(unittest.TestCase):
    # Sampling seems to change at random intervals interesting
    def test_get_public_matches(self):
        self.assertEqual(len(get_public_matches()), 100)

    def test_get_winner(self):
        matches = get_static_public_matches()
        matches = data.convert_data(matches)
        self.assertTrue(radiant_win(matches[0]))
        self.assertFalse(radiant_win(matches[1]))


if __name__ == '__main__':
    unittest.main()
