#!/usr/bin/env python3

import unittest

from stock import Stock


class TestStock(unittest.TestCase):
    def test_sell(self):
        s = Stock('GOOG',100,490.10)

        self.assertEqual(s.shares, 100)
        s.sell(25)
        self.assertEqual(s.shares, 75)

if __name__ == "__main__":
    unittest.main()
