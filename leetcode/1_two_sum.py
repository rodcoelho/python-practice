"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            current = nums[i]

            for j in range(i+1, len(nums)):
                next_c = nums[j]

                if next_c + current == target:
                    return [i, j]
        

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()

        nums = [2,7,11,15]
        target = 9
        expected = [0,1]
        actual = s.twoSum(nums, target)
        self.assertEqual(actual, expected)

        nums = [3,2,4]
        target = 6
        expected = [1,2]
        actual = s.twoSum(nums, target)
        self.assertEqual(actual, expected)

        nums = [3,3]
        target = 6
        expected = [0,1]
        actual = s.twoSum(nums, target)
        self.assertEqual(actual, expected)

unittest.main()
