#!/usr/bin/env python3

import unittest

from readrides import read_rides_as_columns, RideData, read_rides_as_dict_via_columnar
from ex2_2 import ex2_2_q1, ex2_2_q2, ex2_2_q3, ex2_2_q4


class TestEx2(unittest.TestCase):
    rides = read_rides_as_dict_via_columnar("Data/ctabus.csv")
    print(rides[0:10])

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
    unittest.main()