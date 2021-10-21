import unittest
from matches import *


class MatchTestCase(unittest.TestCase):
    # Sampling seems to change at random intervals interesting
    def test_get_public_matches(self):
        self.assertEqual(len(get_public_matches()), 100)

    def test_get_public_ids(self):
        ids = get_public_ids()
        self.assertEqual(type(get_public_ids()), type([]))

    def test_get_games(self):
        # some stuff throws??
        self.assertTrue(len(get_games()) > 90)


if __name__ == '__main__':
    unittest.main()
