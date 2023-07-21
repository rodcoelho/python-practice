#!/usr/bin/env python3

import unittest


class OneCharacterConversionChecker:
	"""Check if string A can be converted to string B with a single edit"""

	def __init__(self):
		pass

	def _diff_checker(self, string1, string2):
		diff = 0
		for i in range(len(string1)):
			if string1[i] != string2[i]:
				diff += 1
		return diff

	def is_convertible(self, string1, string2):
		if len(string1) == len(string2):
			# strings are of same length, no insertion of "_" required
			diff = self._diff_checker(string1, string2)
			if diff > 1:
				return False
			return True

		else:
			# strings are of different lengths, need to normalize s1 and s2
			shorter = None
			longer = None
			if len(string1) < len(string2):
				longer, shorter = string2, string1
			else:
				longer, shorter = string1, string2

			# Add suffix "_" to make shorter >= length of longer to avoid indexing issues during diff check.
			# Superflous suffix will be chopped off anyways so it does not matter if shorter is greater than longer
			diff_in_len = len(longer) - len(shorter)
			suffix = "_" * diff_in_len
			shorter = shorter + suffix

			# insert "_" where there are mismatches to shift rest of string over 1
			for i in range(len(longer)):
				if longer[i] != shorter[i]:
					shorter = shorter[:i] + "_" + shorter[i:]

			diff = self._diff_checker(longer, shorter)

			if diff > 1:
				return False
			return True




class TestOneCharacterConversionChecker(unittest.TestCase):
	def setUp(self):
		self.test_cases = [
			# no changes
			("pale", "pale", True),
			("", "", True),
			# one insert
			("pale", "ple", True),
			("ple", "pale", True),
			("pales", "pale", True),
			("ples", "pales", True),
			("pale", "pkle", True),
			("paleabc", "pleabc", True),
			("", "d", True),
			("d", "de", True),
			# one replace
			("pale", "bale", True),
			("a", "b", True),
			# multiple replace
			("pale", "ble", False),
			("pale", "bake", False),
			# insert and replace
			("pale", "pse", False),
			("pale", "pas", False),
			("pas", "pale", False),
			("pkle", "pable", False),
			("pal", "palks", False),
			("palks", "pal", False),
			# permutation with insert shouldn't match
			("ale", "elas", False),
		]

	def test_OneCharacterConversionChecker_thing(self):
		
		checker = OneCharacterConversionChecker()

		for test_case in self.test_cases:
			string1, string2, expected = test_case
			self.assertEqual(checker.is_convertible(string1, string2), expected, ["Failed ", string1, string2, expected])


if __name__ == "__main__":
	unittest.main()
