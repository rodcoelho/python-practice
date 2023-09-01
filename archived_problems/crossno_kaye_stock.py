#!/usr/bin/env python3

import unittest


class StockMaximizer:
    def maximize(self, prices):
        mini = prices[0]
        maxi = 0

        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] > maxi:
                maxi = prices[i]

        return maxi - mini


class TestStockMaximizer(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([3,4,6,8,9,10], 7),
            ([2,3,4,5,1,99], 98),
            ([10,90,1,7,8,99], 98),
            ([10,90,11,7,8,99], 92),
            ([10,90,11,7,8,99, 1,2], 92),
        ]

    def test_StockMaximizer_maximize(self):

        sm = StockMaximizer()

        for test_case in self.test_cases:

            prices, expected = test_case

            self.assertEqual(sm.maximize(prices), expected, [prices, expected])


if __name__ == "__main__":
    unittest.main()
