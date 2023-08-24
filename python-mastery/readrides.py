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


@measure_memory
def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

