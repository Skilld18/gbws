import unittest
from matches import *
from test_const import *
import hero


class MatchTestCase(unittest.TestCase):
    # Sampling seems to change at random intervals interesting
    def test_get_public_matches(self):
        self.assertEqual(len(get_public_matches()), 100)

    def test_get_winner(self):
        matches = get_static_public_matches()
        matches = data.convert_data(matches)
        self.assertTrue(radiant_win(matches[0]))
        self.assertFalse(radiant_win(matches[1]))

    def test_get_radiant_heroes(self):
        matches = get_static_public_matches()
        matches = data.convert_data(matches)
        game = matches[0]
        expected = {"Tinker", "Witch Doctor", "Bloodseeker", "Faceless Void", "Venomancer"}
        self.assertEqual(get_radiant_heroes_public(game), expected)

    def test_get_dire_heroes(self):
        matches = get_static_public_matches()
        matches = data.convert_data(matches)
        game = matches[0]
        expected = {"Phantom Assassin", "Magnus", "Ember Spirit", "Shadow Shaman", "Wraith King"}
        self.assertEqual(get_dire_heroes_public(game), expected)

    def test_get_heroes_together(self):
        matches = get_static_public_matches()
        matches = data.convert_data(matches)
        together = {}
        testing_hero = "Pudge"
        for m in matches:
            together = hero.get_public_hero_together(testing_hero, m, together)
        print("Hero, Other Hero, Wins, Matches, Percent")
        total_out = []
        for other in hero.get_hero_list():
            if other != testing_hero and frozenset({testing_hero, other, True}) in together:
                wins = together[frozenset({testing_hero, other})]
                matches = together[frozenset({testing_hero, other, True})]
                percent = wins * 100 / matches
                percent = round(percent, 3)
                out = [testing_hero, other, str(wins), str(matches), str(percent)]
                total_out.append(out)
        total_out = sorted(total_out, key=lambda rec: float(rec[4]))
        for o in total_out:
            print(",".join(o))
        self.assertEqual(total_out[-1], ["Pudge", "Snapfire", "1", "1", "100.0"])


if __name__ == '__main__':
    unittest.main()
