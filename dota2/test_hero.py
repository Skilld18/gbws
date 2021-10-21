import unittest
from test_const import *
from hero import *


class TestHero(unittest.TestCase):
    def test_get_hero_name_anti(self):
        self.assertEqual(get_hero_name(1), "Anti-Mage")

    def test_get_hero_name_ax(self):
        self.assertEqual(get_hero_name(2), "Axe")

    def test_get_radiant_heroes(self):
        game = convert_data(get_game_data(known_good_match_id))
        heroes = get_radiant_heroes(game)
        actual = {'Lich', 'Riki', 'Razor', 'Slark', 'Bristleback'}
        self.assertEqual(heroes, actual)

    def test_get_alt_radiant_heroes(self):
        game = convert_data(get_game_data(known_radiant_win))
        heroes = get_radiant_heroes(game)
        actual = {'Drow Ranger', 'Sven', 'Tidehunter', 'Dazzle', 'Windranger'}
        self.assertEqual(heroes, actual)

    def test_get_dire_heroes(self):
        game = convert_data(get_game_data(known_good_match_id))
        heroes = get_dire_heroes(game)
        actual = {'Jakiro', 'Necrophos', 'Lion', 'Viper', 'Dragon Knight'}
        self.assertEqual(actual, heroes)

    def test_get_hero_together(self):
        game = convert_data(get_game_data(known_good_match_id))
        together = {}
        together = get_hero_together("Lich", game, together)
        expected_together = {
            "Lich": 1,
            frozenset({"Riki", "Lich"}): 0,
            frozenset({"Razor", "Lich"}): 0,
            frozenset({"Slark", "Lich"}): 0,
            frozenset({"Bristleback", "Lich"}): 0,
            frozenset({"Riki", "Lich", True}): 1,
            frozenset({"Razor", "Lich", True}): 1,
            frozenset({"Slark", "Lich", True}): 1,
            frozenset({"Bristleback", "Lich", True}): 1,
        }

        self.assertEqual(together, expected_together)

    def test_get_alt_hero_together(self):
        game = convert_data(get_game_data(known_good_match_id))
        together = {}
        together = get_hero_together("Jakiro", game, together)
        expected_together = {
            "Jakiro": 1,
            frozenset({"Jakiro", "Necrophos"}): 1,
            frozenset({"Jakiro", "Lion"}): 1,
            frozenset({"Jakiro", "Viper"}): 1,
            frozenset({"Jakiro", "Dragon Knight"}): 1,
            frozenset({"Jakiro", "Necrophos", True}): 1,
            frozenset({"Jakiro", "Lion", True}): 1,
            frozenset({"Jakiro", "Viper", True}): 1,
            frozenset({"Jakiro", "Dragon Knight", True}): 1,

        }

        self.assertEqual(together, expected_together)

    def test_existing_data(self):
        game = convert_data(get_game_data(known_good_match_id))
        together = {frozenset({"Jakiro", "Lion"}): 3}
        together = get_hero_together("Jakiro", game, together)
        actual = together[frozenset({"Jakiro", "Lion"})]
        self.assertEqual(actual, 4)

    def test_game_count(self):
        game = convert_data(get_game_data(known_good_match_id))
        together = {}
        together = get_hero_together("Razor", game, together)
        together = get_hero_together("Lich", game, together)
        game = convert_data(get_game_data(known_razor_game))
        together = get_hero_together("Razor", game, together)
        together = get_hero_together("Lich", game, together)

        razor_games = get_game_count("Razor", together)
        lich_games = get_game_count("Lich", together)
        self.assertEqual(razor_games, 2)
        self.assertEqual(lich_games, 1)

    def test_get_hero_list(self):
        self.assertTrue(len(get_hero_list()) > 108)
        self.assertTrue("Dazzle" in get_hero_list())
        self.assertTrue("Lion" in get_hero_list())


if __name__ == '__main__':
    unittest.main()
