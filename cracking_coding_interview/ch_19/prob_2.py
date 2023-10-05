# Design an algorithm to figure out if someone has won in a game of tic-toe.

import unittest

class TicTacToe:
    def __init__(self, matrix):
        self.matrix = matrix

    def _diagnose(self, elements):
        first = elements[0]
        for ele in elements:
            if ele != first:
                first = 0
        return first

    def _check_diagnols(self):
        winner = 0 
        ltr = [self.matrix[x][x] for x in range(len(self.matrix))]
        winner += self._diagnose(ltr)
        
        rtl = [self.matrix[x][len(self.matrix)-x-1] for x in range(len(self.matrix))]
        winner += self._diagnose(rtl)
        return winner

    def _check_verticals(self):
        winner = 0
        verts = [[self.matrix[ele][row] for ele in range(len(self.matrix))] for row in range(len(self.matrix))]
        for vert in verts:
            winner += self._diagnose(vert)
        return winner
    
    def _check_horizontals(self):
        winner = 0
        for row in self.matrix:
            winner += self._diagnose(row)
        return winner
    
    def get_winner(self):
        diag = self._check_diagnols()
        vert = self._check_verticals()
        hori = self._check_horizontals()

        winner = diag + vert + hori
        return winner


class TestTTT(unittest.TestCase):
    def test_get_winner(self):
        self.test_cases = [
            ([
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ], 0),
            ([
                [1,1,2],
                [2,1,1],
                [1,2,2]
            ], 0),
            ([
                [1,1,1],
                [0,2,2],
                [0,0,2]
            ], 1),
            ([
                [1,0,0],
                [1,2,2],
                [1,0,2]
            ], 1),
            ([
                [1,2,0],
                [2,1,2],
                [0,2,1]
            ], 1),
        ]
        for test_case in self.test_cases:
            matrix, expected = test_case

            ttt = TicTacToe(matrix)

            self.assertEqual(ttt.get_winner(), expected)

if __name__ == "__main__":
    unittest.main()
