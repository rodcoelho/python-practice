#!/usr/bin/env python3

import unittest


class PermutationChecker:
	def check_permutation_v1(self, string1, string2):
		if len(string2) != len(string1):
			return False

		sorted_s1 = sorted(string1)
		sorted_s2 = sorted(string2)

		if sorted_s1 == sorted_s2:
			return True
		return False

	def check_permutation_v2(self, string1, string2):
		if len(string2) != len(string1):
			return False

		sorted_s1 = sorted(string1)
		sorted_s2 = sorted(string2)

		for i in range(len(sorted_s1)):
			if sorted_s1[i] != sorted_s2[i]:
				return False
		return True


class TestCheckPermutation(unittest.TestCase):
	def setUp(self):
		self.test_cases = (
			("dog", "god", True),
			("abcd", "bacd", True),
			("3563476", "7334566", True),
			("wef34f", "wffe34", True),
			("dogx", "godz", False),
			("abcd", "d2cba", False),
			("2354", "1234", False),
			("dcw4f", "dcw5f", False),
			("DOG", "dog", False),
			("dog ", "dog", False),
			("aaab", "bbba", False),
		)
		self.permutation_checker = PermutationChecker()

	def test_permutation_checker_vN(self):
		for test_case in self.test_cases:
			string1, string2, expected = test_case
			assert self.permutation_checker.check_permutation_v1(string1, string2) == expected
			assert self.permutation_checker.check_permutation_v2(string1, string2) == expected


if __name__ == "__main__":
	unittest.main()
