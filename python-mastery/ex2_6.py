#!/usr/bin/env python3

import unittest

from readrides import DynamicColumnarDataCollection

class TestDynamicColumnarDataCollection(unittest.TestCase):
    def test_collect(self):

        data = DynamicColumnarDataCollection('Data/ctabus.csv', [str, str, str, int])
        data.collect()
        print(data)

        self.assertEqual(len(data), 577563)

        self.assertEqual(data[0], {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354})

        self.assertEqual(data[1], {'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288})

        self.assertEqual(data[2], {'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048})

        # TODO fix slice
        self.assertEqual(data[0:2], {'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048})


if __name__ == "__main__":
    unittest.main()
    