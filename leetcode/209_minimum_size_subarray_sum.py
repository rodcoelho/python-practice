"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
"""

import unittest
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = None
        index = 0


        while index <= len(nums) - 1:
            if nums[index] == target:
                return 1

            # local_index is a way to start one ahead of current index
            local_index = 1
            local_remaining = len(nums[index:])

            # iterate through the current index as start and make slice bigger until we find sum == target
            while local_index <= local_remaining:

                # find where sum of slice is target
                if sum(nums[index:index+local_index]) >= target:                    
                    if min_len is None:
                        min_len = local_index
                    elif min_len > local_index:
                        min_len = local_index

                local_index += 1

            index += 1

        if min_len is None:
            return 0
        return min_len

        
class TestSolution(unittest.TestCase):
    def test_minSubArrayLen(self):
        s = Solution()

        target = 7 
        nums = [2,3,1,2,4,3]
        expected = 2
        actual = s.minSubArrayLen(target, nums)
        self.assertEqual(actual, expected)

        target = 4
        nums = [1,4,4]
        expected = 1
        actual = s.minSubArrayLen(target, nums)
        self.assertEqual(actual, expected)

        target = 11
        nums = [1,1,1,1,1,1,1,1]
        expected = 0
        actual = s.minSubArrayLen(target, nums)
        self.assertEqual(actual, expected)

        target = 11
        nums = [1,2,3,4,5]
        expected = 3
        actual = s.minSubArrayLen(target, nums)
        self.assertEqual(actual, expected)


unittest.main()