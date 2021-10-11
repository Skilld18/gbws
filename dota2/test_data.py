import unittest
import data


class MyTestCase(unittest.TestCase):
    def test_get_game_data(self):
        self.assertNotEqual(data.get_game_data(), None)

    def test_sane_get_game_data(self):
        self.assertIn("dire", data.get_game_data())

    def test_get_key(self):
        self.assertTrue(len(data.get_key()) == 36)

    def test_get_sane_key(self):
        self.assertTrue(len(set(data.get_key())) > 1)


if __name__ == '__main__':
    unittest.main()