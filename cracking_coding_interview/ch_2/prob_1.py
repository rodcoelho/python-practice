#!/usr/bin/env python3

import unittest


class UniqueChecker:
	def __init__(self):
		self.seen_set = set()

	def check(self, string: str) -> bool:
		for char in string:
			if char in self.seen_set:
				return False
			else:
				self.seen_set.add(char)
		return True


class TestUniqueChecker(unittest.TestCase):
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

	def test_UniqueChecker_check(self):
		for test_case in self.test_cases:

			self.c = UniqueChecker()

			string, expected = test_case

			self.assertEqual(self.c.check(string), expected, "fail: {} {}".format(string, expected))


if __name__ == "__main__":
	unittest.main()
