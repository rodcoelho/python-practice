"""
Given two strings ransomNote and magazine, 

return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

import unittest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = {}
        for char in magazine:
            if char in mag_map:
                mag_map[char] += 1
            else:
                mag_map[char] = 1

        for char in ransomNote:
            if char in mag_map and mag_map[char] > 0:
                mag_map[char] -= 1
            else:
                return False
        return True

    
class TestSolution(unittest.TestCase):
    def test_construct(self):
        s = Solution()

        ransomNote = "a"
        magazine = "b"
        expected = False
        actual = s.canConstruct(ransomNote, magazine)
        self.assertEqual(actual, expected)

        ransomNote = "aa"
        magazine = "ab"
        expected = False
        actual = s.canConstruct(ransomNote, magazine)
        self.assertEqual(actual, expected)

        ransomNote = "aa"
        magazine = "aab"
        expected = True
        actual = s.canConstruct(ransomNote, magazine)
        self.assertEqual(actual, expected)


unittest.main()
