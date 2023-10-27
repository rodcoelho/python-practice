"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
import unittest

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        prior_length = 0
        current_length = 0
        prior = " "
        
        for char in s:
            if char == " ":
                if prior != " ":
                    prior_length = current_length
                current_length = 0
            else:
                current_length += 1
            prior = char

        if current_length:
            return current_length
        return prior_length
            

class TestSolution(unittest.TestCase):
    def test_(self):
        solution = Solution()
        
        s = "Hello World"
        expected = 5
        actual = solution.lengthOfLastWord(s)
        self.assertEqual(actual, expected)

        s = "   fly me   to   the moon  "
        expected = 4
        actual = solution.lengthOfLastWord(s)
        self.assertEqual(actual, expected)

        s = "luffy is still joyboy"
        expected = 6
        actual = solution.lengthOfLastWord(s)
        self.assertEqual(actual, expected)

unittest.main()