#!/usr/bin/env python3

import sys
from abc import ABC, abstractmethod

from stock import Portfolio

GENERIC_ROW_FORMAT ="{:>10}"
HEADER_BREAK = "_________"


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        row_format = "".join(GENERIC_ROW_FORMAT for header in headers)
        print(row_format.format(*headers))
        header_break = [HEADER_BREAK for header in headers]
        print(row_format.format(*header_break))

    def row(self, rowdata):
        print(' '.join(GENERIC_ROW_FORMAT.format(d) for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(header for header in headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    header_element = "<th>{}</th>"
    header_div = "<tr> {} </tr>"
    row_element = "<td>{}</td>"
    row_div = "<tr> {} </tr>"
    def headings(self, headers):
        header_elements = " ".join(self.header_element.format(header) for header in headers)
        print(self.header_div.format(header_elements))

    def row(self, rowdata):
        row_elements = " ".join(self.row_element.format(r) for r in rowdata)
        print(self.row_div.format(row_elements))


def create_formatter(name):
    if name == "html":
        formatter_cls = HTMLTableFormatter
    elif name == "csv":
        formatter_cls = CSVTableFormatter
    elif name == "text":
        formatter_cls = TextTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)
    return formatter_cls()

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("formatter is not of TableFormatter type")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file
    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout


portfolio = Portfolio("Data/portfolio.csv")

