#!/usr/bin/env python3

from collections import Counter
import csv

DEFAULT_FILE_PATH = 'Data/portfolio.dat'


class Portfolio:
    def __init__(self, path=DEFAULT_FILE_PATH):
        self.path = path
        self.is_csv = self._file_is_csv()
        self.aggregate_shares = Counter()
        self.portfolio_value = 0
        self.positions = self._get_positions()

    def _get_positions(self):
        return self._read_file()
    
    def _file_is_csv(self):
        return True if self.path.split('.')[-1] == "csv" else False

    def _read_file(self):
        rows = []

        if self.is_csv:
            with open(self.path) as f:
                file = csv.reader(f)
                headers = next(file)
                for ticker, shares, price in file:
                    shares = int(shares)
                    price = float(price)

                    rows.append([ticker, shares, price])
                    self.aggregate_shares[ticker] += shares
        else:
            with open(self.path, 'r') as file:  
                for row in file:
                    try:
                        row = [x for x in row.strip().split(" ") if x]
                        ticker, shares, price = row
                        shares = int(shares)
                        price = float(price)
                        
                        rows.append([ticker, shares, price])
                        self._add_to_portfolio_value(shares, price)
                        self.aggregate_shares[ticker] += shares
                    except Exception as e:
                        print("Couldn't parse: {}".format(row))
                        print("Reason: {}".format(e))
        return rows
    
    def _add_to_portfolio_value(self, shares, price):
        self.portfolio_value += shares * price
    
