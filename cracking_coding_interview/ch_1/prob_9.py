#!/usr/bin/env python3

import unittest


class StringRotator:
	def __init__(self):
		pass

	def rotate_checker(self, s1, s2):
		if len(s1) != len(s2):
			return False

		for i in range(len(s2)):
			if s2[i:] + s2[:i] == s1:
				return True

		return False


class TestStringRotator(unittest.TestCase):
	def setUp(self):
		self.test_cases = [
			("waterbottle", "erbottlewat", True),
			("foo", "bar", False),
			("foo", "foofoo", False),
		]
		self.stringrotator = StringRotator()

	def test_StringRotator_rotate_checker(self):
		for test_case in self.test_cases:

			s1, s2, expected = test_case

			self.assertEqual(self.stringrotator.rotate_checker(s1, s2), expected, ["=Fail", s1, s2, expected])


if __name__ == "__main__":
	unittest.main()
	