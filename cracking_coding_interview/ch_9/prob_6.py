#/usr/bin/env python3

import unittest

# Given a matrix in which each row and each column is sorted,
# write a method to find an element in it.

class MatrixFinder:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def find(self, target):
        row_len, col_len = len(self.matrix)-1, len(self.matrix[0])-1

        # start at the top right
        # this allows us to go down to increase the search and go left to decrease the search
        current = [0, col_len]

        while current[0] <= row_len and current[1] >= 0:

            row, col = current[0], current[1]

            if self.matrix[row][col] == target:
                return current
            if self.matrix[row][col] < target:
                # target if bigger than current, move down
                current = [row+1, col]
            elif self.matrix[row][col] > target:
                # target is smaller than current, move left
                current = [row, col-1]


class TestFinder(unittest.TestCase):
    def test_finder(self):
        self.test_matrix = [
            [3, 6, 10, 13],
            [4, 7, 11, 14],
            [5, 8, 12, 15],
            [9, 16, 17, 21],
        ]
        self.test_cases = [
            [3, [0,0]],
            [4, [1,0]],
            [7, [1,1]],
            [8, [2,1]],
            [15, [2,3]],
            [17, [3,2]],
            [21, [3,3]],
        ]
        mf = MatrixFinder(self.test_matrix)

        for test_case in self.test_cases:
            target, expected = test_case
            
            self.assertEqual(mf.find(target), expected)


if __name__ == "__main__":
    unittest.main()