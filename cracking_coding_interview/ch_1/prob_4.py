#!/usr/bin/env python3

import unittest

class PalimdromePermutator:
	"""
	Determine if the string can be rearranged such that it could be a palimdrome.
	"""
	def __init__(self, string):
		self.string = string.lower()

	def is_palimdrome_permutation(self):
		singles = set()
		for char in self.string:

			if not char.isalpha():
				continue
			
			# check if there are any characters that don't have an even amount of pairs
			if self.string.count(char) % 2 != 0:
				singles.add(char)

		# if there are more than 1 uneven amount of pairs, then it can't be a palindrome
		if len(singles) > 1:
			return False
		return True


class TestPermutator(unittest.TestCase):
	def setUp(self):
		self.test_cases = [
			("aba", True),
			("aab", True),
			("abba", True),
			("aabb", True),
			("a-bba", True),
			("a-bba!", True),
			("Tact Coa", True),
			("jhsabckuj ahjsbckj", True),
			("Able was I ere I saw Elba", True),
			("So patient a nurse to nurse a patient so", False),
			("Random Words", False),
			("Not a Palindrome", False),
			("no x in nixon", True),
			("azAZ", True),
		]

	def test_is_palimdrome_permutation(self):

		for val, expected in self.test_cases:
			self.assertEqual(PalimdromePermutator(val).is_palimdrome_permutation(), expected, ["Failed ", val, expected])

if __name__ == "__main__":
	unittest.main()