#!/usr/bin/env python3

import unittest


class StringCompressor:
	def __init__(self):
		pass

	def compress(self, string):
		final = ""
		prior = ""
		count = 0

		for i in range(len(string)):

			current = string[i]

			# skip the repeats
			if current == prior:
				continue

			else:
				# char is different the prior so let's count
				prior = current
				count = 1
				final += current

				# look into the future
				for char in string[i+1:]:

					# break if new comes up
					if char != current:
						break
					else:
						count += 1

				# add the count
				final += str(count)

		return final if len(final) < len(string) else string


class TestStringCompressor(unittest.TestCase):
	def setUp(self):
		self.test_cases = [
			("aabcccccaaa", "a2b1c5a3"),
			("abcdef", "abcdef"),
			("aabb", "aabb"),
			("aaa", "a3"),
			("a", "a"),
			("", ""),
		]
		self.string_compressor = StringCompressor()

	def test_StringCompressor_compress(self):

		for test_case in self.test_cases:

			string_input, expected = test_case

			self.assertEqual(self.string_compressor.compress(string_input), expected, ["Failed", string_input, expected])


if __name__ == "__main__":
	unittest.main()