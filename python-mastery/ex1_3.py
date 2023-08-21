#!/usr/bin/env python3

import unittest

from pcost import Portfolio


class TestPortfolio(unittest.TestCase):
    def test_Portfolio_position(self):
        p = Portfolio()
        self.assertEqual(p.portfolio_value, 44671.15)


if __name__ == "__main__":
    unittest.main()