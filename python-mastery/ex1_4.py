#!/usr/bin/env python3

import unittest

from ex1_3 import Portfolio

class TestPortfolio(unittest.TestCase):
    def test_Portfolio_position(self):
        p = Portfolio(path='Data/portfolio3.dat')
        self.assertEqual(p.portfolio_value, 12597.479999999998)
    
        p = Portfolio(path='Data/portfolio2.dat')
        self.assertEqual(p.portfolio_value, 19908.75)

if __name__ == "__main__":
    unittest.main()
