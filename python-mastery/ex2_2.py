#!/usr/bin/env python3

import unittest
from collections import Counter

from pcost import Portfolio
from readrides import read_rides_as_dict


def ex2_2_q1(rides):
    """How many bus routes exist in Chicago?"""
    unique_route = set()
    for ride in rides:
        unique_route.add(ride['route'])
    
    return len(unique_route)

def ex2_2_q2(rides, route, date):
    """How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?"""
    day_route_passenger_count = Counter()
    for ride in rides:
        k = ride['route']+ride['date']
        v = ride['rides']
        day_route_passenger_count.update({k:v})
    
    k = route+date
    return day_route_passenger_count[k]

def ex2_2_q3(rides):
    """What is the total number of rides taken on each bus route?"""
    route_passenger_count = Counter()
    for ride in rides:
        k = ride['route']
        v = ride['rides']
        route_passenger_count.update({k:v})
    return route_passenger_count

def ex2_2_q4(rides):
    """What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?"""
    route_passenger_count_2001 = Counter()
    route_passenger_count_2011 = Counter()
    difference = Counter()
    for ride in rides:
        k = ride['route']
        v = ride['rides']
        if ride['date'].endswith("2001"):
            route_passenger_count_2001.update({k:v})
        elif ride['date'].endswith("2011"):
            route_passenger_count_2011.update({k:v})
        else:
            continue
    
    for key, value in route_passenger_count_2011.items():
        print(key, value)
        if key in route_passenger_count_2001:
            difference[key] = route_passenger_count_2011[key] - route_passenger_count_2001[key]
        else:
            difference[key] = route_passenger_count_2011[key]

    return [x[0] for x in difference.most_common(5)]


class TestEx2(unittest.TestCase):
    rides = read_rides_as_dict("Data/ctabus.csv")

    def test_ex2_2_q1(self):
        expected = 181
        result = ex2_2_q1(rides=self.rides)
        self.assertEqual(result, expected)

    def test_ex2_2_q2(self):
        expected = 5055
        result = ex2_2_q2(rides=self.rides, route="22", date="02/02/2011")
        self.assertEqual(result, expected)

    def test_ex2_2_q3(self):
        expected = 133796763
        result = ex2_2_q3(rides=self.rides)
        self.assertEqual(result.most_common(1)[0][1], expected)

    def test_ex2_2_q4(self):
        expected = ['15', '147', '66', '12', '14']
        result = ex2_2_q4(rides=self.rides)
        self.assertEqual(result, expected)

    
if __name__ == "__main__":
    p = Portfolio(path='Data/portfolio.csv')
    print(p.aggregate_shares)

    unittest.main()