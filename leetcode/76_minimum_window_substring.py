"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that 
every character in t (including duplicates) is included in the window. 

If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

import unittest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        elif t == s:
            return t
        
        output = ""
        temp_output = ""

        t_set = set(char for char in t)
        index = 0
        found = 0

        # left to right
        while index <= (len(s) - 1):

            # handle first match w T
            if s[index] in t_set:

                found += 1
                temp_output += s[index]
                
                t_set.remove(s[index])
                
            # handle where we found first occurance but next ele is not match with set
            elif found > 0:
                temp_output += s[index]
            
            if found == len(t):
                if output == "":
                    output = temp_output
                elif len(t) < len(temp_output) < len(output):
                    output = temp_output
                
                # reset couters
                found = 0
                temp_output = ""
                t_set = set(char for char in t)

            index += 1

        # reset couters        
        index = len(s) - 1
        found = 0
        temp_output = ""
        t_set = set(char for char in t)

        # right to left
        while index >= len(t):

            # handle first match
            if s[index] in t_set:

                found += 1
                temp_output += s[index]
                
                t_set.remove(s[index])

            # handle where we found first T but next ele is not match with set
            elif found > 0:
                temp_output += s[index]

            if found == len(t):
                if output == "":
                    output = "".join([char for char in temp_output][::-1])
                elif len(t) < len(temp_output) < len(output):
                    output = "".join([char for char in temp_output][::-1])
                
                # reset couters
                found = 0
                temp_output = ""
        
            index -= 1

        return output


class TestSolution(unittest.TestCase):
    def test_min_window(self):
        solution = Solution()

        s = "abc"
        t = "cba"
        expected = "abc"
        actual = solution.minWindow(s, t)
        self.assertEqual(actual, expected)
        
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        actual = solution.minWindow(s, t)
        self.assertEqual(actual, expected)

        s = "abc"
        t = "ac"
        expected = "abc"
        actual = solution.minWindow(s, t)
        self.assertEqual(actual, expected)

        s = "a"
        t = "a"
        expected = "a"
        actual = solution.minWindow(s, t)
        self.assertEqual(actual, expected)

        s = "a"
        t = "aa"
        expected = ""
        actual = solution.minWindow(s, t)
        self.assertEqual(actual, expected)

unittest.main()
