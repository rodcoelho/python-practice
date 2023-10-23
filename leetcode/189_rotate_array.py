"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

import unittest
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        shift = len(nums) - k
        return nums[shift:] + nums[:shift]

class TestSolution(unittest.TestCase):
    def test_rotate(self):
        s = Solution()

        nums = [1,2,3,4,5,6,7]
        k = 3
        expected = [5,6,7,1,2,3,4]
        actual = s.rotate(nums, k)
        self.assertEqual(actual, expected)

        nums = [-1,-100,3,99]
        k = 2
        expected = [3,99,-1,-100]
        actual = s.rotate(nums, k)
        self.assertEqual(actual, expected)

        nums = [1,2,3,4,5,6,7]
        k = 10
        expected = [5,6,7,1,2,3,4]
        actual = s.rotate(nums, k)
        self.assertEqual(actual, expected)


unittest.main()
