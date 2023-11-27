'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

You may assume all four edges of the grid are all surrounded by water.
'''

import unittest
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        coords_arround = [
            (0,-1), # left
            (0,1),  # right
            (-1,0),  # up
            (1,0), # down
        ]
        positive_one = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                make_surrounding_negative = True if grid[i][j] == "1" else False
                make_current_negative = False
                made_negative = False

                if make_surrounding_negative:

                    positive_one += 1

                    for coords in coords_arround:

                        x = i + coords[0]
                        y = j + coords[1]

                        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                            continue
                        else:
                            
                            if grid[x][y] == "1":
                                grid[x][y] = "-1"
                            elif grid[x][y] == "-1":
                                make_current_negative = True
                
                if make_current_negative and not made_negative:
                    grid[i][j] = "-1"
                    positive_one -= 1
                    made_negative = True

        return positive_one







class TestSolution(unittest.TestCase):
    def testNumIslands(self):
        s = Solution()

        grid = [
            ["1","1","1","1","0"], 
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        expected = 1
        actual = s.numIslands(grid)
        self.assertEqual(actual, expected)

        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        expected = 3
        actual = s.numIslands(grid)
        self.assertEqual(actual, expected)

        grid = [
            ["1","0","1","1","1"],
            ["1","0","0","0","1"],
            ["1","1","1","0","1"]
        ]
        expected = 2
        actual = s.numIslands(grid)
        self.assertEqual(actual, expected)


unittest.main()