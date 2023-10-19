"""
Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.
"""

import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> (int, List[int]):
        non_dupes = len(nums)

        i = 0
        last = None
        dup_found = False

        while i < len(nums):

            # skip "_"
            if nums[i] == "_":
                i += 1
                continue

            # if duplicate found in the last round and is the same, remove and add "_"
            if nums[i] == last and dup_found:
                non_dupes -= 1
                del nums[i]
                nums.append("_")

            # if current is same as last found, let's note it for the next round
            elif nums[i] == last:
                dup_found = True
                last = nums[i]
                i += 1

            # reset dup_found to false and save last found for next round
            elif nums[i] != last:
                dup_found = False
                last = nums[i]
                i += 1

        return (non_dupes, nums)

            
class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        s = Solution()

        nums = [1,1,1,2,2,3]
        expected_k = 5
        expected_nums = [1,1,2,2,3,"_"]
        actual_k, actual_nums = s.removeDuplicates(nums)
        self.assertEqual(actual_k, expected_k)
        self.assertEqual(actual_nums, expected_nums)

        nums = [0,0,1,1,1,1,2,3,3]
        expected_k = 7
        expected_nums = [0,0,1,1,2,3,3,'_','_']
        actual_k, actual_nums = s.removeDuplicates(nums)
        self.assertEqual(actual_k, expected_k)
        self.assertEqual(actual_nums, expected_nums)


unittest.main()
