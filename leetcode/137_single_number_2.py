"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. 

Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

import unittest
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = {}

        for num in nums:
            if num in num_set:
                num_set[num] += 1
            else:
                num_set[num] = 1

            if num_set[num] == 3:
                del num_set[num]

        return list(num_set.keys())[0]


class TestSolution(unittest.TestCase):
    def testSingleNumber(self):
        s = Solution()

        nums = [2,2,3,2]
        expected =  3
        actual = s.singleNumber(nums)
        self.assertEqual(actual, expected)

        nums = [0,1,0,1,0,1,99]
        expected = 99
        actual = s.singleNumber(nums)
        self.assertEqual(actual, expected)

unittest.main()