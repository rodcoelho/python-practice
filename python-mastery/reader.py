#!/usr/bin/env python3

import csv
from sys import intern

from malloc import measure_memory

@measure_memory
def read_csv_as_dicts(path, coltypes):
    final = []
    with open(path) as f:
        file = csv.reader(f)
        headers = next(file)
        return [{key: func(val) for key, val, func in zip(headers, row, coltypes)} for row in file]

print(read_csv_as_dicts('Data/portfolio.csv', [str,int,float]))

print(read_csv_as_dicts('Data/ctabus.csv', [str,str,str,int])[0])

print(read_csv_as_dicts('Data/ctabus.csv', [intern, intern ,str,int])[0])