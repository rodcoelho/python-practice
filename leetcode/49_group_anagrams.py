"""
Given an array of strings strs, group the anagrams together. 

You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

import unittest

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}

        for s in strs:

            normalized_sort = "".join(sorted([char for char in s]))

            if normalized_sort in sorted_map:
                sorted_map[normalized_sort].append(s)

            else:
                sorted_map[normalized_sort] = [s]
        
        return [val for val in sorted_map.values()]


class TestSolution(unittest.TestCase):
    def test_groupAnagrams(self):
        s = Solution()

        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        actual = s.groupAnagrams(strs)
        self.assertEqual(actual, expected)

        strs = [""]
        expected = [[""]]
        actual = s.groupAnagrams(strs)
        self.assertEqual(actual, expected)

        strs = ["a"]
        expected = [["a"]]
        actual = s.groupAnagrams(strs)
        self.assertEqual(actual, expected)


unittest.main()