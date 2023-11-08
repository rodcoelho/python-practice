"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana_map = {}
        for char in s:
            if char in ana_map:
                ana_map[char] += 1
            else:
                ana_map[char] = 1

        for char in t:
            if char not in ana_map:
                return False

            else:
                ana_map[char] -= 1

                if ana_map[char] == 0:
                    del ana_map[char]

        if len(ana_map) > 0:
            return False
        return True


class TestSolution(unittest.TestCase):
    def test_is_anagram(self):
        solution = Solution()

        s = "anagram"
        t = "nagaram"
        expected = True
        actual = solution.isAnagram(s, t)
        self.assertEqual(actual, expected)

        s = "rat"
        t = "car"
        expected = False
        actual = solution.isAnagram(s, t)
        self.assertEqual(actual, expected)


unittest.main()
        