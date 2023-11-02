"""
Given a string s, find the length of the longest substring without repeating characters.
"""

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) in [0, 1]:
            return len(s)

        output = ""
        index = 0

        while index <= len(s) - 1:

            current = s[index]
            local_output_max = current
            local_set = set()
            local_set.add(current)

            remaining = len(s[index:]) - 1
            local_index = 1

            while local_index <= remaining:

                if s[local_index+index] not in local_set:
                    local_set.add(s[local_index+index])
                    local_output_max += s[local_index+index]
                else:
                    local_index = remaining + 1

                local_index += 1

            if len(local_output_max) > len(output):
                    output = local_output_max

            index += 1

        return len(output)
        

class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()

        s = "abcabcbb"
        expected = 3
        actual = solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual, expected)

        s = "bbbbb"
        expected = 1
        actual = solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual, expected)

        s = "pwwkew"
        expected = 3
        actual = solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual, expected)


unittest.main()
