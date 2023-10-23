"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""

import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        expected = 5
        actual = s.maxProfit(prices)
        self.assertEqual(actual, expected)
        
        prices = [7,6,4,3,1]
        expected = 0
        actual = s.maxProfit(prices)
        self.assertEqual(actual, expected)

        prices = [7,1,5,3,6,4,2,20]
        expected = 19
        actual = s.maxProfit(prices)
        self.assertEqual(actual, expected)

        prices = [7,2,5,3,6,4,1,20]
        expected = 19
        actual = s.maxProfit(prices)
        self.assertEqual(actual, expected)


unittest.main()
