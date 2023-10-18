"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
"""

from typing import List
import unittest


class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        final = []

        for i in range(len(nums1) + len(nums2)):
            if nums1 and nums2:
                if nums1[0] <= nums2[0]:
                    final.append(nums1[0])
                    nums1 = nums1[1:]
                elif nums1[0] >= nums2[0]:
                    final.append(nums2[0])
                    nums2 = nums2[1:]
                
            elif nums1:
                final.append(nums1[0])
                nums1 = nums1[1:]
            elif nums2:
                final.append(nums2[0])
                nums2 = nums2[1:]

        return final, nums2
        

class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        nums1 = [1, 2,3]
        nums2 = [2, 5,6]
        expected = [1,2,2,3,5,6]
        nums1, nums2 = s.merge(nums1, nums2)
        self.assertEqual(nums1, expected)

        nums1 = [2,5,6]
        nums2 = [1,2,3]
        expected = [1,2,2,3,5,6]
        nums1, nums2 = s.merge(nums1, nums2)
        self.assertEqual(nums1, expected)

        nums1 = [1]
        nums2 = []
        expected = [1]
        nums1, nums2 = s.merge(nums1, nums2)
        self.assertEqual(nums1, expected)

        nums1 = []
        nums2 = [1]
        expected = [1]
        nums1, nums2 = s.merge(nums1, nums2)
        self.assertEqual(nums1, expected)

        nums1 = [2,7,8,14]
        nums2 = [1,2,3,4,5,6,9,10]
        expected = [1,2,2,3,4,5,6,7,8,9,10,14]
        nums1, nums2 = s.merge(nums1, nums2)
        self.assertEqual(nums1, expected)


unittest.main()