import unittest
from hero import *


class TestHero(unittest.TestCase):
    def test_get_hero_name_anti(self):
        self.assertEqual(get_hero_name(1), "Anti-Mage")

    def test_get_hero_name_ax(self):
        self.assertEqual(get_hero_name(2), "Axe")


if __name__ == '__main__':
    unittest.main()
