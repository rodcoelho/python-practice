#!/usr/bin/env python3

import csv

from malloc import measure_memory
from readrides import read_rides_as_tuples, read_rides_as_dict, read_rides_as_class, read_rides_as_named_tuple, read_rides_as_class_with_slots, read_rides_as_columns


if __name__ == '__main__':
    tuple_rows = read_rides_as_tuples('Data/ctabus.csv')
    dict_rows = read_rides_as_dict('Data/ctabus.csv')
    class_rows = read_rides_as_class('Data/ctabus.csv')
    named_tuple_rows = read_rides_as_named_tuple('Data/ctabus.csv')
    class_with_slots_rows = read_rides_as_class_with_slots('Data/ctabus.csv')
    column_rows = read_rides_as_columns('Data/ctabus.csv')

    """
    Function Name       : read_rides_as_tuples
    Current memory usage: 123.687486MB
    Peak                : 123.718104MB

    Function Name       : read_rides_as_dict
    Current memory usage: 188.375334MB
    Peak                : 188.406008MB

    Function Name       : read_rides_as_class
    Current memory usage: 142.173438MB
    Peak                : 142.20404MB

    Function Name       : read_rides_as_named_tuple
    Current memory usage: 128.308878MB
    Peak                : 128.339472MB

    Function Name       : read_rides_as_class_with_slots
    Current memory usage: 119.067974MB
    Peak                : 119.09856MB

    Function Name       : read_rides_as_columns
    Current memory usage: 96.16867MB
    Peak                : 96.19924MB
    """
