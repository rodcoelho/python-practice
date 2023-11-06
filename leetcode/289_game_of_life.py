"""
The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

The board is made up of an m x n grid of cells, where each cell has an initial state: 
live (represented by a 1) or dead (represented by a 0). 

Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules:

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
        0 - 1 neighbors
        Live -> Dead

    Any live cell with two or three live neighbors lives on to the next generation.
        2 - 3 neighbors
        Live -> Live

    Any live cell with more than three live neighbors dies, as if by over-population.
        4 - 8 neighbors
        Live -> Dead

    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        3 neighbors
        Dead -> Live

The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously. 

Given the current state of the m x n grid board, 
return the next state.
"""

import unittest
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> List[List[int]]:
        coords = [
            (-1,-1), (-1,0), (-1,1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        to_live = []
        to_die = []

        for i in range(len(board)):
            for j in range(len(board[0])):

                current = board[i][j]

                live_neighbors = 0

                for coord in coords:

                    x_coord, y_coord = coord

                    spot_x, spot_y = x_coord+i, y_coord+j 

                    if len(board)-1 < spot_x or spot_x < 0 or len(board[0])-1 < spot_y or spot_y < 0:
                        continue
                    
                    live_neighbors += board[spot_x][spot_y]

                if 0 <= live_neighbors <= 1 and current == 1:
                    to_die.append((i,j))
                
                elif 4 <= live_neighbors <= 8 and current == 1:
                    to_die.append((i,j))

                elif live_neighbors == 3 and current == 0:
                    to_live.append((i,j))

        for coord in to_live:
            x, y = coord
            board[x][y] = 1
        
        for coord in to_die:
            x, y = coord
            board[x][y] = 0

        return board

        
class TestSolution(unittest.TestCase):
    def test_gameOfLife(self):
        s = Solution()

        board = [
            [0,1,0],
            [0,0,1],   
            [1,1,1],
            [0,0,0]
        ]
        expected = [
            [0,0,0],
            [1,0,1],
            [0,1,1],
            [0,1,0]
        ]
        actual = s.gameOfLife(board)
        self.assertEqual(actual, expected)

        board = [
            [1,1],
            [1,0]
        ]
        expected = [
            [1,1],
            [1,1]
        ]
        actual = s.gameOfLife(board)
        self.assertEqual(actual, expected)


unittest.main()
