#!/usr/bin/env python3

import csv

class Portfolio:
    def __init__(self, filename):
        self.filename = filename
        self.stocks = []
        self.headers = []
        self.read_portfolio()

    def _add_to_portfolio(self, rows):
        for row in rows:
            self.stocks.append(Stock.from_row(row))

    def read_portfolio(self):
        if self.filename.split('.')[-1] == "csv":
            with open(self.filename) as raw_file:
                rows = csv.reader(raw_file)        
                self.headers = next(rows)
                self._add_to_portfolio(rows)

        else:
            with open(self.filename, 'r') as raw_file:
                self.headers = next(the_file)
                rows = ([x for x in row.strip().split(" ") if x] for row in raw_file)
                self._add_to_portfolio(rows)
        
        return self.stocks
    
    def print_portfolio(self):
        print('%10s %10s %10s' % (self.headers[0], self.headers[1], self.headers[2]))
        print('%10s %10s %10s' % ('_________', '_________', '_________'))
        for s in self.stocks:
            print('%10s %10s %10s' % (s.name, s.shares, s.price))

            

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        vals = (func(val) for func, val in zip(cls.types, row))
        return cls(*vals)

    def cost(self):
        return self.shares * self.price

    def sell(self, quantity):
        if quantity <= self.shares:
            self.shares -= quantity

if __name__ == "__main__":
    portfolio = Portfolio("Data/portfolio.csv")
    portfolio.print_portfolio()

    s = Stock.from_row(['AA', '100', '75'])
    print(s.cost())
    
    

    