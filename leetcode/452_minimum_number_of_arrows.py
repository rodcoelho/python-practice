"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane.
The balloons are represented as a 2D integer array points 
where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. 

You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 

A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 

There is no limit to the number of arrows that can be shot. 

A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""

from typing import List
import unittest

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        left_to_right = self.find_overlap(points)
        right_to_left = self.find_overlap(points[::-1])

        return min(left_to_right, right_to_left)

    def find_overlap(self, points: List[List[int]]) -> int:
        final = [points[0]]

        for i in range(1,len(points)):
            current_p = points[i]

            overlap = False

            for j in range(len(final)):
                current_final = final[j]

                #  cf     cp       new
                # [1,5] [2,2] --> 2,2

                #  cf     cp       new
                # [1,4] [3,5] --> 3,4

                #  cf     cp       new
                # [1,5] [3,4] --> 3,4
                if current_final[0] <= current_p[0] <= current_final[1]:
                    final[j] = [current_p[0], min(current_p[0], current_final[1])]
                    overlap = True
                    break

                #  cf     cp       new
                # [1,5] [5,6] --> 5,5
                elif current_p[0] == current_final[1]:
                    final[j] = [current_p[0], current_p[0]]
                    overlap = True
                    break
                

                #  cf     cp       new
                # [2,5] [1,2] --> 2,2
                elif current_p[1] == current_final[0]:
                    final[j] = [current_p[1], current_p[1]]
                    overlap = True
                    break
            
            if not overlap:
                final.append(current_p)

        return len(final)


class TestSolution(unittest.TestCase):
    def testFindMinArrowShots(self):
        s = Solution()

        points = [[10,16],[2,8],[1,6],[7,12]]
        expected = 2
        actual = s.findMinArrowShots(points)
        self.assertEqual(actual, expected)

        points = [[1,2],[3,4],[5,6],[7,8]]
        expected = 4
        actual = s.findMinArrowShots(points)
        self.assertEqual(actual, expected)

        points = [[1,2],[2,3],[3,4],[4,5]]
        expected = 2
        actual = s.findMinArrowShots(points)
        self.assertEqual(actual, expected)


unittest.main()