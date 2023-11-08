"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""

import unittest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        normalized_pattern = [char for char in pattern]
        normalized_string = [word for word in s.split(" ")]

        if len(normalized_pattern) != len(normalized_string):
            return False
        
        pattern_to_string_map = {}
        string_to_pattern_map = {}
        string_to_pattern = ""

        for i in range(len(normalized_pattern)):

            if normalized_pattern[i] in pattern_to_string_map:
                if pattern_to_string_map[normalized_pattern[i]] != normalized_string[i]:
                    return False
                string_to_pattern += normalized_pattern[i]

            else:
                pattern_to_string_map[normalized_pattern[i]] = normalized_string[i]
                string_to_pattern += normalized_pattern[i]

            string_to_pattern_map[normalized_string[i]] = normalized_pattern[i]

        if string_to_pattern == pattern and len(string_to_pattern_map.keys()) == len(pattern_to_string_map.keys()):
            return True
        return False


class TestSolution(unittest.TestCase):
    def test_word_pattern(self):
        solution = Solution()

        pattern = "abba"
        s = "dog cat cat dog"
        expected = True
        actual = solution.wordPattern(pattern, s)
        self.assertEqual(actual, expected)

        pattern = "abba"
        s = "dog cat cat fish"
        expected = False
        actual = solution.wordPattern(pattern, s)
        self.assertEqual(actual, expected)

        pattern = "aaaa"
        s = "dog cat cat dog"
        expected = False
        actual = solution.wordPattern(pattern, s)
        self.assertEqual(actual, expected)

        pattern = "abba"
        s = "dog dog dog dog"
        expected = False
        actual = solution.wordPattern(pattern, s)
        self.assertEqual(actual, expected)


unittest.main()
