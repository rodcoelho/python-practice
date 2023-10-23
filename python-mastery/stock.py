#!/usr/bin/env python3

import csv
from decimal import Decimal
from validate import PositiveInteger, PositiveFloat, NonEmptyString, DecimalType

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
    __slots__ = ('name','_shares','_price')
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    def __repr__(self):
        # Note: The !r format code produces the repr() string
        return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))

class DecimalStock(Stock):
    # _types = (str, int, Decimal)
    # def __init__(self, name, shares, price):
    #     self.name = name
    #     self.shares = shares
    #     self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = DecimalType.check(value)


if __name__ == "__main__":
    portfolio = Portfolio("Data/portfolio.csv")
    portfolio.print_portfolio()

    s = Stock.from_row(['AA', 100, 75.0])
    # print(s.cost)
    
    s = Stock("GOOG", 10, 100.0)
    # print(s.cost)

    s = DecimalStock("AAPL", 100, Decimal(101.0))
    # print(s.cost)

    