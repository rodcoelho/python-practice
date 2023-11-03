"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. 
"acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. 
You can return the answer in any order.
"""

import unittest
from typing import List
import itertools

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        occurances = []
        perms = ["".join(list(perm)) for perm in itertools.permutations(words)]
        perm_len = len(perms[0])
        
        index = 0

        while index <= len(s):

            current_window = s[index:index+perm_len]

            if current_window in perms:
                occurances.append(index)
        
            index += 1

        return occurances
                

class TestSolution(unittest.TestCase):
    def test_findSubstring(self):
        solution = Solution()

        s = "barfoothefoobarman"
        words = ["foo","bar"]
        expected = [0,9]
        actual = solution.findSubstring(s, words)
        self.assertEqual(actual, expected)

        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        expected = []
        actual = solution.findSubstring(s, words)
        self.assertEqual(actual, expected)

        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        expected = [6,9,12]
        actual = solution.findSubstring(s, words)
        self.assertEqual(actual, expected)


unittest.main()