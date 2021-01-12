import unittest
from bracket import *


class TestBracket(unittest.TestCase):
    def setUp(self):
        self.bracket = Bracket(0, 100, 0.5)
        self.weird_bracket = Bracket(1, 345, 0.25)

    def test_bracket(self):
        with self.assertRaises(TypeError):
            # noinspection PyArgumentList
            Bracket()
        with self.assertRaises(ValueError):
            Bracket(0, 0, 0)

    def test_str(self):
        bracket_str = "             0 <= income <            100 taxed at 0.5"
        self.assertEqual(str(self.bracket), bracket_str)
        bracket_str = "             1 <= income <            345 taxed at 0.25"
        self.assertEqual(str(self.weird_bracket), bracket_str)

    def test_taxable(self):
        self.assertEqual(self.bracket.taxable(0), 0)
        self.assertEqual(self.bracket.taxable(1000), 100)
        self.assertEqual(self.weird_bracket.taxable(0.5), 0)
        self.assertEqual(self.weird_bracket.taxable(1000), 344)
        self.assertEqual(Bracket(100, 200, 0.25).taxable(150), 50)

    def test_apply(self):
        self.assertEqual(self.bracket.apply(0), 0)
        with self.assertRaises(ValueError):
            self.bracket.apply(1000)
        self.assertEqual(self.weird_bracket.apply(100), 25)

    def test_calc_bracket(self):
        self.assertEqual(self.bracket.calc_bracket(0), 0)
        self.assertEqual(self.weird_bracket.calc_bracket(100), 25)
        self.assertEqual(self.weird_bracket.calc_bracket(1000), round(344 * 0.25))

    def test_lt(self):
        self.assertTrue(self.bracket.__lt__(self.weird_bracket))
        self.assertFalse(self.weird_bracket.__lt__(self.bracket))

    def test_valid_brackets(self):
        bracket_list = [self.weird_bracket, self.bracket]
        with self.assertRaises(ValueError):
            Bracket.valid_brackets(bracket_list)
        sorted_list = Bracket.sort_brackets(bracket_list)
        self.assertEqual([self.bracket, self.weird_bracket],
                         Bracket.sort_brackets(bracket_list))
        with self.assertRaises(ValueError):
            Bracket.valid_brackets(sorted_list)
        b345 = Bracket(345, 346, 0)
        bracket_list = Bracket.sort_brackets([b345, self.weird_bracket])
        with self.assertRaises(ValueError):
            Bracket.valid_brackets(bracket_list)
        b0345 = Bracket(0, 345, 0)
        bracket_list = sorted([b345, b0345])
        with self.assertRaises(ValueError):
            Bracket.valid_brackets(bracket_list)

        bracket_list = [Bracket(0, sys.maxsize, 0)]
        self.assertTrue(Bracket.valid_brackets(bracket_list))

    def test_calc_brackets(self):
        with self.assertRaises(IndexError):
            Bracket.calc_brackets(0, [])
        self.assertEqual(Bracket.calc_brackets(0, [Bracket(0, sys.maxsize, 0)]), 0)
        value = Bracket.calc_brackets(100, [Bracket(0, sys.maxsize, 0.25)])
        self.assertEqual(25, value)
