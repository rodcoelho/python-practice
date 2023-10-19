"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

"""

from typing import List
import unittest


class Solution:
    def majorityElement_efficient(self, nums: List[int]) -> int:
        highest_count = 0
        highest_value = None

        for num in nums:
            if highest_count == 0:
                highest_value = num

            if num == highest_value:
                highest_count += 1
            else:
                highest_count -= 1

        return highest_value

    def majorityElement_with_dict(self, nums: List[int]) -> int:
        highest_count = 0
        highest_value = None

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            if count[num] > highest_count:
                highest_count = count[num]
                highest_value = num
        
        return highest_value


class TestSolution(unittest.TestCase):
    def test_majorityElement(self):
        s = Solution()

        nums = [3,2,3]
        expected = 3
        actual = s.majorityElement_with_dict(nums)
        self.assertEqual(actual, expected)
        actual = s.majorityElement_efficient(nums)
        self.assertEqual(actual, expected)
        

        nums = [2,2,1,1,1,2,2]
        expected = 2
        actual = s.majorityElement_with_dict(nums)
        self.assertEqual(actual, expected)
        actual = s.majorityElement_efficient(nums)
        self.assertEqual(actual, expected)
        

        nums = [3,3,4,2,4,4,2,4,4]
        expected = 4
        actual = s.majorityElement_with_dict(nums)
        self.assertEqual(actual, expected)
        actual = s.majorityElement_efficient(nums)
        self.assertEqual(actual, expected)
        
unittest.main()
