"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
"""

from typing import List
import unittest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        final = [[0 for ele in row] for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                final[j][len(matrix) - i - 1] = matrix[i][j]
        return final
        
class TestSolution(unittest.TestCase):
    def test_rotate(self):
        s = Solution()
       
        matrix = [
            [1,2,3],  # 00 01 02 - 02 12 22
            [4,5,6],  # 10 11 12 - 01 11 21
            [7,8,9],  # 20 21 22 - 00 10 20
        ]
        expected = [
            [7,4,1],  # 02 12 22
            [8,5,2],  # 01 11 21
            [9,6,3],  # 00 10 20
        ]
        actual = s.rotate(matrix)
        self.assertEqual(actual, expected)

        matrix = [
            [5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]
        ]
        expected = [
            [15,13,2,5],
            [14,3,4,1],
            [12,6,8,9],
            [16,7,10,11]
        ]
        actual = s.rotate(matrix)
        self.assertEqual(actual, expected)
        

unittest.main()