#!/usr/bin/env python3

import csv
import collections

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


@measure_memory
def read_rides_as_dict_via_columnar(filename, types):
    '''
    # Custom columnar type that we can add dicts to and will save as columnar storage

    RideData:
        routes = []
        dates = []
        daytypes = []
        numrides = []
        
    '''
    headers = ['route', 'date', 'daytype', 'rides']
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            record = {
                header:func(data) for data, header, func in zip(row, headers, types)
            }
            records.append(record)
    return records


class DynamicColumnarData:
    def __init__(self):
        self._attributes = []

    def __len__(self):
        if self._attributes:
            return len(getattr(self, self._attributes[0]))
        else:
            return 0

    def __getitem__(self, index):
        if isinstance(index, int):
            return { 
                attr: getattr(self, attr)[index] for attr in self._attributes
            }
        elif isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            step = 1 if step is None else step
            return [
                {attr: getattr(self, attr)[x] for attr in self._attributes}
                for x in range(start, stop, step)
            ]

    def append(self, d):
        for attr, val in d.items():
            current = getattr(self, attr)
            current.append(val)
            setattr(self, attr, current)


class DynamicColumnarDataCollection(collections.abc.Sequence):
    def __init__(self, filename, types):
        self.filename = filename
        self.is_csv = self._file_is_csv()
        
        self.file = None
        self.headers = None
        self.types = types

        self.data = DynamicColumnarData()
        
        
    def _file_is_csv(self):
        return True if self.filename.split('.')[-1] == "csv" else False

    def _add_dynamic_attributes(self):
        """set header as attributes with empty lists"""
        for x in range(len(self.headers)):
            setattr(self.data, self.headers[x], [])
            self.data._attributes.append(self.headers[x])

    def collect(self):
        if self._file_is_csv:
            with open(self.filename) as the_file:
                self.file = csv.reader(the_file)
                self.headers = next(self.file)
                self._aggregate_data()
            
        else:
            with open(self.filename, 'r') as the_file:
                self.headers = next(self.file)
                self.file = ([x for x in row.strip().split(" ") if x] for row in self.file)
                self._aggregate_data()

    def _aggregate_data(self):
        self._add_dynamic_attributes()

        for line in self.file:
            self.data.append({key:func(val) for key, val, func in zip(self.headers, line, self.types)})


    def __getitem__(self, index):
        if isinstance(index, int):
            return self.data[index]
        elif isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            step = 1 if step is None else step
            return self.data[start, stop, step]

    def __len__(self):
        return len(self.data)


class RideData(collections.abc.Sequence):
    """
    Columnar storage of each row
    """
    def __init__(self):
        # Columns
        self.routes = []      
        self.dates = []
        self.daytypes = []
        self.numrides = []
        
    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, int):
            return { 
                'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index] 
            }
        elif isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            step = 1 if step is None else step
            return [
                {
                    "route": self.routes[x],
                    "date": self.dates[x],
                    "daytype": self.daytypes[x],
                    "ride": self.numrides[x],
                }
                for x in range(start, stop, step)
            ]

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


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

