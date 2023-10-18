#!/usr/bin/env python3

import csv
from sys import intern
from abc import ABC, abstractmethod

from malloc import measure_memory
from stock import Stock, Portfolio
from readrides import RowClassType


class CSVParser(ABC):
    def parse(self, path):
        records = []
        with open(path) as f:
            file = csv.reader(f)
            self.headers = next(file)
            for row in file:
                record = self.make_record(row)
                records.append(record)

        return records
    
    @abstractmethod
    def make_record(self, row):
        pass
    
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, row):
        return {key: func(val) for key, val, func in zip(self.headers, row, self.types)}

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls
    
    def make_record(self, row):
        return self.cls.from_row(row)


@measure_memory
def read_csv_as_dicts(path, coltypes):
    # final = []
    # with open(path) as f:
    #     file = csv.reader(f)
    #     headers = next(file)
    #     return [{key: func(val) for key, val, func in zip(headers, row, coltypes)} for row in file]
    dict_csv_reader = DictCSVParser(coltypes)
    print(dict_csv_reader.parse(path))

    
def read_csv_as_instances(path, cls):
    # instances = []
    # with open(path) as f:
    #     file = csv.reader(f)
    #     headers = next(file)
    #     for row in file:
    #         instances.append(cls.from_row(row))    
    # return instances
    instance_csv_reader = InstanceCSVParser(cls)
    return instance_csv_reader.parse(path)


if __name__ == "__main__":
    print(read_csv_as_dicts('Data/portfolio.csv', [str,int,float]))
    # dict_csv_reader = DictCSVParser([str,int,float])
    # print(dict_csv_reader.parse('Data/portfolio.csv'))

    print(read_csv_as_dicts('Data/ctabus.csv', [str,str,str,int])[0])
    # dict_csv_reader = DictCSVParser([str,str,str,int])
    # print(dict_csv_reader.parse('Data/ctabus.csv')[0])

    print(read_csv_as_dicts('Data/ctabus.csv', [intern, intern ,str,int])[0])
    # dict_csv_reader = DictCSVParser([intern, intern ,str,int])
    # print(dict_csv_reader.parse('Data/ctabus.csv')[0])

    print(read_csv_as_instances('Data/portfolio.csv', Stock))
    # instance_csv_reader = InstanceCSVParser(Stock)
    # print(instance_csv_reader.parse('Data/portfolio.csv'))

    print(len(read_csv_as_instances('Data/ctabus.csv', RowClassType)))
    # instance_csv_reader = InstanceCSVParser(RowClassType)
    # print(len(instance_csv_reader.parse('Data/ctabus.csv')))
