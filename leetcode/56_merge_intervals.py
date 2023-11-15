"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

import unittest
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        final = [intervals[0]]

        count = 1

        while count <= len(intervals) - 1:

            current = intervals[count]
            beg_current = current[0]
            end_current = current[1]

            # iterate through final to see if we should inject

            injected = False

            for i in range(len(final)):

                beg_final = final[i][0]
                end_final = final[i][1]
                # print("ENTER")
                # print("current", current)
                # print("final", final)

                if beg_final <= beg_current <= end_final <= end_current:
                    # print("IF 1")
                    final[i] = [beg_final, end_current]
                    injected = True

                elif beg_current <= beg_final <= end_current <= end_final:
                    # print("IF 2")
                    final[i] = [beg_current, end_final]
                    injected = True

                elif beg_current <= beg_final <= end_final <= end_current:
                    # print("IF 2")
                    final[i] = [beg_current, end_current]
                    injected = True
                
                elif beg_final <= beg_current <= end_current <= end_final:
                    # print("IF 2")
                    final[i] = [beg_final, end_final]
                    injected = True

            # if no injections, append to end
            if not injected:
                final.append(current)

            count += 1
        
        return final


class TestSolution(unittest.TestCase):
    def test_merge(self):
        s = Solution()

        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        actual = s.merge(intervals)
        self.assertEqual(actual, expected)

        intervals = [[2,6],[1,3],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        actual = s.merge(intervals)
        self.assertEqual(actual, expected)

        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        actual = s.merge(intervals)
        self.assertEqual(actual, expected)

        intervals = [[1,4],[2,3]]
        expected = [[1,4]]
        actual = s.merge(intervals)
        self.assertEqual(actual, expected)

        intervals = [[2,3],[1,4]]
        expected = [[1,4]]
        actual = s.merge(intervals)
        self.assertEqual(actual, expected)


unittest.main()