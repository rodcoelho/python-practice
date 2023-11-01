"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        left_max = height[left_index]
        right_index = len(height) - 1
        right_max = height[right_index]
        
        max_found = (right_index - left_index) * min(left_max, right_max)

        checked = len(height) - 1

        while checked >= 0:
            current_local_max = (right_index - left_index) * min(height[left_index], height[right_index])

            # check local max if we move right or left
            try:
                left_local_max = (right_index - left_index - 1) * min(height[left_index + 1], height[right_index])
                right_local_max = (right_index - left_index - 1) * min(height[left_index], height[right_index - 1])
            except IndexError:
                checked = -1
                continue
            
            # left goes right
            if left_local_max >= current_local_max:
                left_index += 1

            # right goes left
            elif current_local_max <= right_local_max:
                right_index -= 1

            else:
                # didn't move right or left, let's move both
                left_index += 1
                right_index -= 1

            # check for new max
            local_max = (right_index - left_index) * min(height[left_index], height[right_index])
            if local_max > max_found:
                max_found = local_max

            checked -= 1

        return max_found


class TestSolution(unittest.TestCase):
    def test_most_water(self):
        s = Solution()

        height = [1,2,4,3]
        expected = 4
        actual = s.maxArea(height)
        self.assertEqual(actual, expected)

        height = [1,8,6,2,5,4,8,3,7]
        expected = 49
        actual = s.maxArea(height)
        self.assertEqual(actual, expected)

        height = [1,1]
        expected = 1
        actual = s.maxArea(height)
        self.assertEqual(actual, expected)

        height = [2,3,4,5,18,17,6]
        expected = 17
        actual = s.maxArea(height)
        self.assertEqual(actual, expected)


unittest.main()
