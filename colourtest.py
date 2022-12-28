import unittest
import itertools
from lib import is_purple


class ColourTest(unittest.TestCase):

    def test_purple(self):
        cases = itertools.product([True, False], repeat=3)
        purple = (True, False, True)
        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(is_purple(*case), case == purple)


if __name__ == '__main__':
    unittest.main()
