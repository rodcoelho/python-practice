"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 

Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

import unittest
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        found = False
        right = len(numbers) - 1
        left = 0
        
        while not found:

            if numbers[right] + numbers[left] == target:
                return [right + 1, left + 1]
            
            else:



class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        s = Solution()

        numbers = [1,2,3,4,5,6,7]
        target = 9
        expected = [1,2]
        actual = s.twoSum(numbers, target)
        self.assertEqual(actual, expected)

        numbers = [2,7,11,15]
        target = 9
        expected = [1,2]
        actual = s.twoSum(numbers, target)
        self.assertEqual(actual, expected)

        numbers = [2,3,4]
        target = 6
        expected = [1,3]
        actual = s.twoSum(numbers, target)
        self.assertEqual(actual, expected)

        numbers = [-1,0]
        target = -1
        expected = [1,2]
        actual = s.twoSum(numbers, target)
        self.assertEqual(actual, expected)

unittest.main()