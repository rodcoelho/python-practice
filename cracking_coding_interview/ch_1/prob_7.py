#!/usr/bin/env python3

import unittest


class MatrixRotator:
	def __init__(self):
		pass

	def rotate(self, matrix):
		row_len = len(matrix)
		final = [["" for y in range(row_len)] for x in range(row_len)]

		for i, j in zip(range(row_len), range(row_len - 1, -1, -1)):
			for k in range(row_len):
				final[k][i] = matrix[j][k]

		return final


class TestMatrixRotator(unittest.TestCase):
	def setUp(self):
		self.test_cases = [
			(
				[
					[1, 2, 3], 
					[4, 5, 6], 
					[7, 8, 9]
				],
				[
					[7, 4, 1], 
					[8, 5, 2], 
					[9, 6, 3]
				]
			),
			(
				[
					[1, 2, 3, 4, 5], 
					[6, 7, 8, 9, 10],
					[11, 12, 13, 14, 15],
					[16, 17, 18, 19, 20],
					[21, 22, 23, 24, 25],
				],
				[
					[21, 16, 11, 6, 1],
					[22, 17, 12, 7, 2],
					[23, 18, 13, 8, 3],
					[24, 19, 14, 9, 4],
					[25, 20, 15, 10, 5],
				],
			),
		]

	def test_MatrixRotator_rotate(self):
		rotator = MatrixRotator()
		for test_case in self.test_cases:

			matrix, expected = test_case
			self.assertEqual(rotator.rotate(matrix), expected, ["Fail", matrix, expected])


if __name__ == "__main__":
	unittest.main()
