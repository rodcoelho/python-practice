#!/usr/bin/env python3

import unittest


class Portfolio:
    def __init__(self):
        self.portfolio_value = 0
        self.positions = self._get_positions()

    def _get_positions(self):
        return self._read_file()

    def _read_file(self):
        rows = []
        with open('Data/portfolio.dat', 'r') as file:
            for row in file:
                ticker, shares, price = row.strip().split(" ")
                shares, price = int(shares), float(price)
                rows.append([ticker, shares, price])
                self._add_to_portfolio_value(shares, price)
        return rows
    
    def _add_to_portfolio_value(self, shares, price):
        self.portfolio_value += shares * price


class TestPortfolio(unittest.TestCase):
    def test_Portfolio_get_value(self):
        p = Portfolio()
        self.assertEqual(p.portfolio_value, 44671.15)
        print(p.positions)


if __name__ == "__main__":
    unittest.main()