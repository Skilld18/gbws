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
        actual = set()
        actual.add("Lich")
        actual.add("Riki")
        actual.add("Razor")
        actual.add("Slark")
        actual.add("Bristleback")
        self.assertEqual(heroes, actual)

    def test_get_alt_radiant_heroes(self):
        game = convert_data(get_game_data(known_radiant_win))
        heroes = get_radiant_heroes(game)
        actual = set()
        actual.add("Drow Ranger")
        actual.add("Sven")
        actual.add("Tidehunter")
        actual.add("Dazzle")
        actual.add("Windranger")
        self.assertEqual(heroes, actual)

    def test_get_dire_heroes(self):
        game = convert_data(get_game_data(known_good_match_id))
        heroes = get_dire_heroes(game)
        actual = set()
        actual.add("Jakiro")
        actual.add("Necrophos")
        actual.add("Lion")
        actual.add("Viper")
        actual.add("Dragon Knight")
        self.assertEqual(actual, heroes)


if __name__ == '__main__':
    unittest.main()
