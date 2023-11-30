"""
You are given two strings word1 and word2. 

Merge the strings by adding letters in alternating order, starting with word1. 

If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

import unittest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""

        max_len = max(len(word1), len(word2))

        for i in range(max_len):

            try:
                final += word1[i]
            except IndexError:
                pass

            try:
                final += word2[i]
            except IndexError:
                pass
        
        return final


class TestSolution(unittest.TestCase):
    def testMergeAlternately(self):
        s = Solution()

        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"
        actual = s.mergeAlternately(word1, word2)
        self.assertEqual(actual, expected)

        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"
        actual = s.mergeAlternately(word1, word2)
        self.assertEqual(actual, expected)

        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"
        actual = s.mergeAlternately(word1, word2)
        self.assertEqual(actual, expected)


unittest.main()