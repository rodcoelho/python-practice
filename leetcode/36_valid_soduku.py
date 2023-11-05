"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List
import unittest


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal
        for row in board:
            row_set = set()
            for num in row:
                if num not in row_set:
                    if num != ".":
                        row_set.add(num)
                else:
                    return False

        # check vertical
        for i in range(len(board)):
            col_set = set()
            for j in range(len(board)):
                num = board[j][i]
                if num not in col_set:
                    if num != ".":
                        col_set.add(num)
                else:
                    return False

        return True


class TestSolution(unittest.TestCase):
    def test_is_valid(self):
        s = Solution()
        
        board = [
            ["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
            ]
        expected = True
        actual = s.isValidSudoku(board)
        self.assertEqual(actual, expected)

        board = [
            ["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
        ]
        expected = False
        actual = s.isValidSudoku(board)
        self.assertEqual(actual, expected)

        
        board = [
            [".",".",".",".","5",".",".","1","."],
            [".","4",".","3",".",".",".",".","."],
            [".",".",".",".",".","3",".",".","1"],
            ["8",".",".",".",".",".",".","2","."],
            [".",".","2",".","7",".",".",".","."],
            [".","1","5",".",".",".",".",".","."],
            [".",".",".",".",".","2",".",".","."],
            [".","2",".","9",".",".",".",".","."],
            [".",".","4",".",".",".",".",".","."]
        ]
        expected = True
        actual = s.isValidSudoku(board)
        self.assertEqual(actual, expected)

unittest.main()