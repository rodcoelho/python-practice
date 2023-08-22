#!/usr/bin/env python3

from pcost import Portfolio

if __name__ == "__main__":
    p = Portfolio(path='Data/portfolio.csv')
    print(p.aggregate_shares)
