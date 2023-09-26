#!/usr/bin/env python3

from stock import Portfolio

GENERIC_ROW_FORMAT ="{:>10}"
HEADER_BREAK = "_________"

def print_table(rows, columns):
    row_format = "".join(GENERIC_ROW_FORMAT for column in columns)
    print(row_format.format(*columns))
    header_break = [HEADER_BREAK for column in columns]
    print(row_format.format(*header_break))

    for row in rows:
        vals = [getattr(row, col) for col in columns]
        print(row_format.format(*vals))


portfolio = Portfolio("Data/portfolio.csv")
print_table(portfolio.stocks, ['name', 'shares','price'])
