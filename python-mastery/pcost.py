#!/usr/bin/env python3

DEFAULT_FILE_PATH = 'Data/portfolio.dat'


class Portfolio:
    def __init__(self, path=DEFAULT_FILE_PATH):
        self.path = path
        self.portfolio_value = 0
        self.positions = self._get_positions()

    def _get_positions(self):
        return self._read_file()

    def _read_file(self):
        rows = []
        with open(self.path, 'r') as file:
            
            for row in file:
                try:
                    row = [x for x in row.strip().split(" ") if x]
                    ticker, shares, price = row
                    shares, price = int(shares), float(price)
                    rows.append([ticker, shares, price])
                    self._add_to_portfolio_value(shares, price)
                except Exception as e:
                    print("Couldn't parse: {}".format(row))
                    print("Reason: {}".format(e))
        return rows
    
    def _add_to_portfolio_value(self, shares, price):
        self.portfolio_value += shares * price