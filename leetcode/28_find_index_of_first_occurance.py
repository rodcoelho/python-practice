"""
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""

import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        hay_len = len(haystack)
        nee_len = len(needle)

        count = 0
        while count < hay_len:
            
            if haystack[count] == needle[0]:

                needle_count = 1
                matches = 1
                while needle_count < nee_len:
                    
                    try:
                        if needle[needle_count] == haystack[count + needle_count]:
                            matches += 1
                    except IndexError:
                        return -1

                    needle_count += 1

                if matches == nee_len:
                    return count
            
            count += 1
        return -1


class TestSolution(unittest.TestCase):
    def test_index_occurance(self):
        s = Solution()

        haystack = "dadbutsad"
        needle = "sad"
        expected = 6
        actual = s.strStr(haystack, needle)
        self.assertEqual(expected, actual)

        haystack = "sadbutsad"
        needle = "sad"
        expected = 0
        actual = s.strStr(haystack, needle)
        self.assertEqual(expected, actual)

        haystack = "leetcode"
        needle = "leeto"
        expected = -1
        actual = s.strStr(haystack, needle)
        self.assertEqual(expected, actual)

        haystack = "aaa"
        needle = "aaaa"
        expected = -1
        actual = s.strStr(haystack, needle)
        self.assertEqual(expected, actual)

unittest.main()