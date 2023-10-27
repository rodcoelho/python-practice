"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List
import unittest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        words = len(strs)
        prefix_finding = True
        common = ""

        index = 0
        while prefix_finding:
            count = 1
            first = None
            for s in strs:
                try:
                    if not first:
                        first = s[index]
                    else:

                        if s[index] == first:
                            count += 1
                except IndexError:
                    prefix_finding = False
                    continue

            if count == words and prefix_finding:
                common += first
            else:
                prefix_finding = False
            index += 1

        return common


class TestSolution(unittest.TestCase):
    def test_longestCommonPrefix(self):
        s = Solution()

        strs = ["flower","flow","flight"]
        expected = "fl"
        actual = s.longestCommonPrefix(strs)
        self.assertEqual(actual, expected)

        strs = ["dog","racecar","car"]
        expected = ""
        actual = s.longestCommonPrefix(strs)
        self.assertEqual(actual, expected)

unittest.main()