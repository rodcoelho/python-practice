"""
You are given an array of non-overlapping intervals intervals where 

intervals[i] = [starti, endi] represent the start and the end of the ith interval and 

intervals is sorted in ascending order by starti. 

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and 

intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

from hmac import new
import unittest
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = []
        during = [newInterval]
        after = []

        beg_new_int, end_new_int = newInterval

        for interval in intervals:
            
            beg_int, end_int = interval

            # before
            if end_int < beg_new_int:
                before.append(interval)

            # after
            elif beg_int > end_new_int:
                after.append(interval)

            # during (merge)
            else:
                during.append(interval)

        new_beg = None
        new_end = None
        for interval in during:
            beg_int, end_int = interval
            if new_beg is None and new_end is None:
                new_beg = beg_int
                new_end = end_int
                continue
                
            if beg_int < new_beg:
                new_beg = beg_int
            if end_int > new_end:
                new_end = end_int
        
        return before + [[new_beg, new_end]] + after
        

class TestSolution(unittest.TestCase):
    def test_insert(self):
        s = Solution()
        
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        expected = [[1,5],[6,9]]
        actual = s.insert(intervals, newInterval)
        self.assertEqual(actual, expected)

        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        expected = [[1,2],[3,10],[12,16]]
        actual = s.insert(intervals, newInterval)
        self.assertEqual(actual, expected)


unittest.main()