"""
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

import unittest
from typing import List


class Solution:
    def canJump(self, nums:List[int]) -> bool:
        current_index = 0
        last_index = 0
        to_jump = 0
        count = 0

        for i in range(len(nums)):
            try:
                to_jump = nums[current_index]
            except IndexError:
                count += to_jump
                break
            last_index = current_index
            current_index = current_index + to_jump
            count += to_jump
        
        if count >= len(nums):
            return True
        return False
            

class TestSolution(unittest.TestCase):
    def test_canJump(self):
        s = Solution()
    
        nums = [2,3,1,1,4]
        expected = True
        actual = s.canJump(nums)
        self.assertEqual(actual, expected)
        
        nums = [3,2,1,0,4]
        expected = False
        actual = s.canJump(nums)
        self.assertEqual(actual, expected)

        nums = [4,0,0,0,2,0,1,10,0,0,0,0,0,0,0]
        expected = True
        actual = s.canJump(nums)
        self.assertEqual(actual, expected)

        nums = [4,0,0,0,2,0,1,3,0,0,0]
        expected = False
        actual = s.canJump(nums)
        self.assertEqual(actual, expected)

        nums = [4,0,0,0,2,0,1,4,0,0,0]
        expected = True
        actual = s.canJump(nums)
        self.assertEqual(actual, expected)


unittest.main()