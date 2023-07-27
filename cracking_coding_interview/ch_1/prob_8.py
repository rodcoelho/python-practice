#!/usr/bin/env python3

import unittest

class Nuker(object):
	"""If there's a nuke_val in a row or a column, nuke the row or column to the nuke_val"""
	def __init__(self):
		pass

	def nuke(self, matrix, nuke_val):
		size = len(matrix)
		row_nuke = set()
		col_nuke = set()

		for i in range(size):
			for j in range(size):
				if matrix[i][j] == nuke_val:
					row_nuke.add(i)
					col_nuke.add(j)

		for i in range(size):
			for j in range(size):
				if i in row_nuke or j in col_nuke:
					matrix[i][j] = nuke_val

		return matrix

		

class TestNuker(unittest.TestCase):
	def setUp(self):
		self.test_cases = [[
			[
				[1, 2, 3, 4, 0],
				[6, 0, 8, 9, 10],
				[11, 12, 13, 14, 15],
				[16, 0, 18, 19, 20],
				[21, 22, 23, 24, 25],
			],
			[
				[0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0],
				[11, 0, 13, 14, 0],
				[0, 0, 0, 0, 0],
				[21, 0, 23, 24, 0],
			],
		]]

	def test_Nuker_zero(self):
		nuker = Nuker()
		for test_case in self.test_cases:
			matrix, expected = test_case

			self.assertEqual(nuker.nuke(matrix, 0), expected, ["fail", matrix, expected])

if __name__ == "__main__":
	unittest.main()