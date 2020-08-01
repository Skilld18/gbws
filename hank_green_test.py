#!/usr/bin/python3

import unittest
import hank_green as hg

class TestStringMethods(unittest.TestCase):

    def test_ends_in_ly(self):
        self.assertTrue(hg.ends_in_ly("Beautifully"))
        self.assertFalse(hg.ends_in_ly("Bad"))
        self.assertFalse(hg.ends_in_ly("A"))
        self.assertFalse(hg.ends_in_ly(3))
    
    def test_nsyl(self):
        self.assertEqual(hg.nsyl("idea"), 3)
        self.assertEqual(hg.nsyl("a"), 1)
        self.assertEqual(hg.nsyl("catastrophic"), 4)


if __name__ == '__main__':
    unittest.main()

