"""
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

import unittest
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        max_len = 0

        for n in nums:

            if n - 1 not in num_set:

                current = n
                current_len = 1

                while current + 1 in num_set:
                    current += 1
                    current_len += 1

                if current_len > max_len:
                    max_len = current_len
        return max_len
    

class TestSolution(unittest.TestCase):
    def test_longestConsecutive(self):
        s = Solution()

        nums = [100,4,200,1,3,2]
        expected = 4
        actual = s.longestConsecutive(nums)
        self.assertEqual(actual, expected)

        nums = [0,3,7,2,5,8,4,6,0,1]
        expected = 9
        actual = s.longestConsecutive(nums)
        self.assertEqual(actual, expected)


unittest.main()