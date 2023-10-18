"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
"""

import unittest
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> (int, List[int]):
        non_matches = len(nums)
        i = 0

        while i < len(nums):
            if nums[i] == val:
                # if a match, sub from non_match, delete element, don't move on to next i, add _
                non_matches -= 1
                del nums[i]
                nums.append("_")
            else:
                # not a match, move to next element
                i += 1
        
        return non_matches, nums


class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        s = Solution()

        nums = [3,2,2,3]
        val = 3
        expected_k = 2
        expected_nums = [2,2,"_","_"]
        actual_k, actual_nums = s.removeElement(nums, val)
        self.assertEqual(actual_k, expected_k)
        self.assertEqual(actual_nums, expected_nums)
        
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        expected_k = 5
        expected_nums = [0,1,3,0,4,"_","_","_"]
        actual_k, actual_nums = s.removeElement(nums, val)
        self.assertEqual(actual_k, expected_k)
        self.assertEqual(actual_nums, expected_nums)
        

unittest.main()