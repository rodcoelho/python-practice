#!/usr/bin/env python3

import unittest


class InfectionMatrix:
    def __init__(self):
        self.matrix = [
        [1,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,1],
    ]

    def increase_spread(self):
        coordinates = []

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    coordinates.append((i,j))

        for coord in coordinates:
            self._infect(coord[0], coord[1])

    def _infect(self, row, col):
        surrounding = (
            (-1,-1),
            (-1,0),
            (-1,1),
            (0,-1),
            (0,1),
            (1,-1),
            (1,0),
            (1,1),
        )
        for coord in surrounding:
            try:
                self.matrix[row+coord[0]][col+coord[1]] = 1
            except Exception as e:
                pass


class TestMatrixInfection(unittest.TestCase):
    def test_matrix_increase_spread(self):
        im = InfectionMatrix()
        im.increase_spread()
        self.assertEqual(
            im.matrix,
            [
                [1,1,0,0,0,0,0,0,1,1],
                [1,1,0,0,0,0,0,0,1,1],
                [0,0,1,1,1,0,0,0,0,0],
                [0,0,1,1,1,0,0,0,0,0],
                [0,0,1,1,1,0,0,0,0,0],
                [0,0,1,1,1,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,0,0],
                [0,0,0,0,0,1,1,1,0,0],
                [1,1,0,0,0,1,1,1,1,1],
                [1,1,0,0,0,0,0,0,1,1],
            ]
        )

        im.increase_spread()
        self.assertEqual(
            im.matrix,
            [
                [1,1,1,0,0,0,0,1,1,1],
                [1,1,1,1,1,1,0,1,1,1],
                [1,1,1,1,1,1,0,1,1,1],
                [0,1,1,1,1,1,0,0,0,0],
                [0,1,1,1,1,1,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,0],
                [1,1,1,0,1,1,1,1,1,1],
                [1,1,1,0,1,1,1,1,1,1],
                [1,1,1,0,1,1,1,1,1,1],

            ]
        )


if __name__ == "__main__":
    unittest.main()
        