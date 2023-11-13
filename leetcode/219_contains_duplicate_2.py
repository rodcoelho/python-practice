"""
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

import unittest
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums) - 1):

            for j in range(i+1, i+k+1):
                try:
                    if nums[i] == nums[j]:
                        return True
                except IndexError:
                    continue
            
        return False


class TestSolution(unittest.TestCase):
    def testcontainsNearbyDuplicate(self):
        s = Solution()

        nums = [1,2,3,1]
        k = 3
        expected = True
        actual = s.containsNearbyDuplicate(nums, k)
        self.assertEqual(actual, expected)

        nums = [1,0,1,1]
        k = 1
        expected = True
        actual = s.containsNearbyDuplicate(nums, k)
        self.assertEqual(actual, expected)

        nums = [1,2,3,1,2,3]
        k = 2
        expected = False
        actual = s.containsNearbyDuplicate(nums, k)
        self.assertEqual(actual, expected)


unittest.main()
