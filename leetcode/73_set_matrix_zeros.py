"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

from typing import List
import unittest


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = []
        cols = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows:
                    matrix[i][j] = 0
                if j in cols:
                    matrix[i][j] = 0

        return matrix


class TestSolution(unittest.TestCase):
    def test_setZeros(self):
        s = Solution()

        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        expected = [[1,0,1],[0,0,0],[1,0,1]]
        actual = s.setZeroes(matrix)
        self.assertEqual(actual, expected)

        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        actual = s.setZeroes(matrix)
        self.assertEqual(actual, expected)


unittest.main()