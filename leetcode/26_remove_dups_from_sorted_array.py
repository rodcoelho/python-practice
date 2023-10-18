"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.
"""

import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> (int, List[int]):
        non_under = len(nums)
        prior = None
        i = 0

        while i < len(nums):

            # handle first case, make prior and move on
            if prior is None:
                prior = nums[i]
                i += 1

            else:
                # if match with prior and not under, remove non_under, del item, add under
                if nums[i] == prior and nums[i] != '_':
                    non_under -= 1
                    del nums[i]
                    nums.append("_")

                # not match, update prior, move on
                else:
                    prior = nums[i]
                    i += 1

        return non_under, nums


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_dups(self):
        s = Solution()

        nums = [1,1,2]
        expected_k = 2
        expected_nums = [1,2,"_"]
        actual_k, actual_nums = s.removeDuplicates(nums)
        self.assertEqual(actual_k, expected_k)
        self.assertEqual(actual_nums, expected_nums)

        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_k = 5
        expected_nums = [0,1,2,3,4,"_","_","_","_","_"]
        actual_k, actual_nums = s.removeDuplicates(nums)
        self.assertEqual(actual_k, expected_k)
        self.assertEqual(actual_nums, expected_nums)

        
unittest.main()
