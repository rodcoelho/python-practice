"""
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time.
"""

import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for num in nums:
            product *= num
        
        for i in range(len(nums)):
            nums[i] = int(product / nums[i])
            
        return nums

 
class TestSolution(unittest.TestCase):
    def test_product_except_self(self):
        s = Solution()

        nums = [1,2,3,4]
        expected = [24,12,8,6]
        actual = s.productExceptSelf(nums)
        self.assertEqual(actual, expected)

        nums = [1,-2,3,-4]
        expected = [24,-12,8,-6]
        actual = s.productExceptSelf(nums)
        self.assertEqual(actual, expected)


unittest.main()