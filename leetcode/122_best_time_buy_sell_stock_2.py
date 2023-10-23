"""
You are given an integer array prices 
where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold_long_profit = self.hold_long(prices)
        hold_short_profit = self.hold_short(prices)

        if hold_long_profit > hold_short_profit:
            return hold_long_profit
        return hold_short_profit

    def hold_short(self, prices: List[int]) -> int:
        short_profit = 0

        i = 1
        while i < len(prices):
            short_gain = prices[i] - prices[i-1]
            if short_gain > 0:
                short_profit += short_gain
            i += 1

        return short_profit

    def hold_long(self, prices: List[int]) -> int:
        best_profit = 0
        left_min = prices[0]
        right_max = prices[0]
        
        i = 0
        
        while i < len(prices):
            
            current = prices[i]

            if current < left_min:
                left_min = current
                right_max = current

            if current > right_max:
                right_max = current
                current_profit = right_max - left_min

                if current_profit > best_profit:
                    best_profit = current_profit

            i += 1

        return best_profit

        
class TestSolution(unittest.TestCase):
    def test_maxProfit(self):
        s = Solution()

        prices = [7,1,5,3,6,4]
        expected = 7
        actual = s.maxProfit(prices)
        self.assertEqual(actual, expected)

        prices = [1,2,3,4,5]
        expected = 4
        actual = s.maxProfit(prices)
        self.assertEqual(actual, expected)

        prices = [7,6,5,4,3]
        expected = 0
        actual = s.maxProfit(prices)
        self.assertEqual(actual, expected)
        

unittest.main()
