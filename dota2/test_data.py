import unittest
import data


class MyTestCase(unittest.TestCase):
    def test_get_game(self):
        self.assertNotEqual(data.get_game(), None)


if __name__ == '__main__':
    unittest.main()
