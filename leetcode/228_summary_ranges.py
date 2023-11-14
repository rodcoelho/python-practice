"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

from math import exp
import unittest 
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        final = []

        tmp = [nums[0]]
        next_increment = nums[0] + 1

        index = 1

        while index < len(nums):

            # check if next_increment == current
            current = nums[index]
            if current == next_increment:

                # add to temp and set next increment to look for
                tmp.append(current)
                next_increment = current + 1

            # if not equal, then make tmp into normalized -> format, append to final, reset temp, prep for next itter
            else:
                # package tmp to add to final
                if len(tmp) == 1:
                    final.append(str(tmp[0]))
                else:
                    final.append(str(tmp[0]) + "->" + str(tmp[-1]))

                # reset tmp, calculate next increment
                tmp = [current]
                next_increment = current + 1
            
            index += 1

        # get any last members of tmp to final
        if tmp:
            if len(tmp) == 1:
                final.append(str(tmp[0]))
            else:
                final.append(str(tmp[0]) + "->" + str(tmp[-1]))
        
        return final
        


class TestSolution(unittest.TestCase):
    def testSummaryRanges(self):
        s = Solution()

        nums = [0,1,2,4,5,7]
        expected = ["0->2","4->5","7"]
        actual = s.summaryRanges(nums)
        self.assertEqual(actual, expected)

        nums = [0,2,3,4,6,8,9]
        expected = ["0","2->4","6","8->9"]
        actual = s.summaryRanges(nums)
        self.assertEqual(actual, expected)

unittest.main()
