import unittest
from test_const import *
from data import *
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
        together = get_hero_together("Lich", game)
        expected_together = dict()
        expected_together[frozenset({"Riki", "Lich"})] = 0
        expected_together[frozenset({"Razor", "Lich"})] = 0
        expected_together[frozenset({"Slark", "Lich"})] = 0
        expected_together[frozenset({"Bristleback", "Lich"})] = 0
        self.assertEqual(together, expected_together)

    def test_get_alt_hero_together(self):
        game = convert_data(get_game_data(known_good_match_id))
        together = get_hero_together("Jakiro", game)
        expected_together = dict()
        expected_together[frozenset({"Jakiro", "Necrophos"})] = 1
        expected_together[frozenset({"Jakiro", "Lion"})] = 1
        expected_together[frozenset({"Jakiro", "Viper"})] = 1
        expected_together[frozenset({"Jakiro", "Dragon Knight"})] = 1
        self.assertEqual(together, expected_together)




if __name__ == '__main__':
    unittest.main()
