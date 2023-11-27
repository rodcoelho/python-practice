"""
Given a non-empty array of integers nums, every element appears twice except for one. 

Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

import unittest
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()

        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)

        return list(num_set)[0]


class TestSolution(unittest.TestCase):
    def testSingleNumber(self):
        s = Solution()

        nums = [2,2,1]
        expected =  1
        actual = s.singleNumber(nums)
        self.assertEqual(actual, expected)

        nums = [4,1,2,1,2]
        expected = 4
        actual = s.singleNumber(nums)
        self.assertEqual(actual, expected)

        nums = [1]
        expected = 1
        actual = s.singleNumber(nums)
        self.assertEqual(actual, expected)

unittest.main()