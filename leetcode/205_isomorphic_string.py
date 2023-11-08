"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. 

No two characters may map to the same character, but a character may map to itself.
"""

import unittest

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        final = ""
        iso_map_s_to_t = {}
        iso_map_t_to_s = {}

        for i in range(len(s)):

            if s[i] in iso_map_s_to_t and iso_map_s_to_t[s[i]] != t[i]:
                return False
            if t[i] in iso_map_t_to_s and iso_map_t_to_s[t[i]] != s[i]:
                return False
            iso_map_s_to_t[s[i]] = t[i]
            iso_map_t_to_s[t[i]] = s[i]

        for key, value in iso_map_s_to_t.items():
            if key != iso_map_t_to_s[value]:
                return False
        
        for key, value in iso_map_t_to_s.items():
            if key != iso_map_s_to_t[value]:
                return False
            
        return True
        

class TestSolution(unittest.TestCase):
    def testIsSomorphic(self):
        solution = Solution()

        s = "egg"
        t = "add"
        expected = True
        actual = solution.isIsomorphic(s, t)
        self.assertEqual(actual, expected)

        s = "foo"
        t = "bar"
        expected = False
        actual = solution.isIsomorphic(s, t)
        self.assertEqual(actual, expected)

        s = "paper"
        t = "title"
        expected = True
        actual = solution.isIsomorphic(s, t)
        self.assertEqual(actual, expected)

        s = "foo"
        t = "bar"
        expected = False
        actual = solution.isIsomorphic(s, t)
        self.assertEqual(actual, expected)

        s = "badc"
        t = "baba"
        expected = False
        actual = solution.isIsomorphic(s, t)
        self.assertEqual(actual, expected)

        s = "bbbaaaba"
        t = "aaabbbba"
        expected = False
        actual = solution.isIsomorphic(s, t)
        self.assertEqual(actual, expected)


unittest.main()