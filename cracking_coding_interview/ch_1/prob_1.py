#!/usr/bin/env python3

import unittest

class UniqueChecker:
	def characters_are_unique_v1(self, string: str) -> bool:
		num_of_chars = len(string)
		final_set = len(set(char for char in string))

		if num_of_chars == final_set:
			return True
		return False

	def characters_are_unique_v2(self, string: str) -> bool:
		chars_checked = set()
		for char in string:
			if char in chars_checked:
				return False
			chars_checked.add(char)
		return True

class TestAdditionFunction(unittest.TestCase):
	def setUp(self):
		self.test_cases = [
			("abcd", True),
			("s4fad", True),
			("", True),
			("23ds2", False),
			("hb 627jh=j ()", False),
			("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
			("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
			]
		self.unique_checker = UniqueChecker()

	def test_characters_are_unique_vN(self):
		for test_case in self.test_cases:
			test_string, expected_value = test_case
			assert self.unique_checker.characters_are_unique_v1(test_string) == expected_value, test_string
			assert self.unique_checker.characters_are_unique_v2(test_string) == expected_value, test_string



if __name__ == "__main__":
	unittest.main()
