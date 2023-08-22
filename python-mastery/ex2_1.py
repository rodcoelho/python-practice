#!/usr/bin/env python3

import csv

from malloc import measure_memory


@measure_memory
def read_rides_as_tuples(filename):
    '''
    # A tuple
    row = (route, date, daytype, rides)

    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


@measure_memory
def read_rides_as_dict(filename):
    '''
    # A dictionary
    row = {
        'route': route,
        'date': date,
        'daytype': daytype,
        'rides': rides,
    }

    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records

# A class
class RowClassType:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

@measure_memory
def read_rides_as_class(filename):
    '''
    # A class
    class RowClassType:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowClassType(route=route, date=date, daytype=daytype, rides=rides)
            records.append(record)
    return records

# A named tuple
from collections import namedtuple
RowNamedTuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

@measure_memory
def read_rides_as_named_tuple(filename):
    '''
    # A named tuple
    from collections import namedtuple
    RowNamedTuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowNamedTuple(route=route, date=date, daytype=daytype, rides=rides)
            records.append(record)
    return records

# A class with __slots__
class RowClassWithSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

@measure_memory
def read_rides_as_class_with_slots(filename):
    '''
    # A class with __slots__
    class RowClassWithSlots:
        __slots__ = ['route', 'date', 'daytype', 'rides']
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowClassWithSlots(route=route, date=date, daytype=daytype, rides=rides)
            records.append(record)
    return records


if __name__ == '__main__':
    tuple_rows = read_rides_as_tuples('Data/ctabus.csv')
    dict_rows = read_rides_as_dict('Data/ctabus.csv')
    class_rows = read_rides_as_class('Data/ctabus.csv')
    named_tuple_rows = read_rides_as_named_tuple('Data/ctabus.csv')
    class_with_slots_rows = read_rides_as_class_with_slots('Data/ctabus.csv')

    """
    Function Name       : read_rides_as_tuples
    Current memory usage: 123.68799MB
    Peak                : 123.718608MB

    Function Name       : read_rides_as_dict
    Current memory usage: 188.375334MB
    Peak                : 188.406008MB

    Function Name       : read_rides_as_class
    Current memory usage: 142.173438MB
    Peak                : 142.20404MB

    Function Name       : read_rides_as_named_tuple
    Current memory usage: 128.308822MB
    Peak                : 128.339416MB

    Function Name       : read_rides_as_class_with_slots
    Current memory usage: 119.067918MB
    Peak                : 119.098504MB
    """
