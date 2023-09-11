#!/usr/bin/env python3

import unittest
from pprint import pprint

class Battleship:
    def __init__(self):
        self.size = 10
        self.board = {
            1: [[0 for y in range(self.size)] for x in range(self.size)],
            2: [[0 for y in range(self.size)] for x in range(self.size)]
        }
        self.ship_placements = {
            1: {
                2: [],
                3: [],
                4: []
            },
            2: {
                2: [],
                3: [],
                4: []
            }
        }
    
    def place_ship(self, player, row, col, size, horizontal=True):
        board = self.board[player]
        if self._can_place_ship(player, row, col, size, horizontal):
            if horizontal:
                for i in range(size):
                    board[row][col+i] = size

                    self.ship_placements[player][size].append((row, col+i))
            else:
                for i in range(size):
                    board[row+i][col] = size

                    self.ship_placements[player][size].append((row + i, col))

    def _can_place_ship(self, player, row, col, size, horizontal=True):
        board = self.board[player]
        if horizontal:
            try:
                for i in range(size):
                    spot = board[row][col+i]
                    if spot != 0:
                        return False
                return True
            except Exception as e:
                return False
        else:
            try:
                for i in range(size):
                    spot = board[row+i][col]
                    if spot != 0:
                        return False
                return True
            except Exception as e:
                return False


class TestBattleship(unittest.TestCase):
    def test_battleship_place_ship(self):
        bs = Battleship()        

        bs.place_ship(1, 1, 1, 4)
        self.assertEqual(
            bs.board[1], 
            [[0,0,0,0,0,0,0,0,0,0],
            [0,4,4,4,4,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],],
            )
        
        bs.place_ship(1, 2, 2, 3, horizontal=False)
        self.assertEqual(
            bs.board[1], 
            [[0,0,0,0,0,0,0,0,0,0],
            [0,4,4,4,4,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],],
            )

        bs.place_ship(1, 1, 9, 2)
        self.assertEqual(
            bs.board[1], 
            [[0,0,0,0,0,0,0,0,0,0],
            [0,4,4,4,4,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],],
            )

        bs.place_ship(1, 1, 9, 2, horizontal=False)
        self.assertEqual(
            bs.board[1], 
            [[0,0,0,0,0,0,0,0,0,0],
            [0,4,4,4,4,0,0,0,0,2],
            [0,0,3,0,0,0,0,0,0,2],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],],
            )
        
        self.assertEqual(
            bs.ship_placements, 
            {
                1: {
                    2: [(1,9), (2,9)],
                    3: [(2,2), (3,2), (4,2)],
                    4: [(1,1), (1,2), (1,3), (1,4)],
                },
                2: {
                    2: [],
                    3: [],
                    4: [],
                },
            }
            )

if __name__ == "__main__":
    unittest.main()
