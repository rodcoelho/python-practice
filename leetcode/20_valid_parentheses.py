"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        opens = {"(": ")", "[": "]", "{": "}"}
        closes = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            if char in opens:
                stack.append(char)
            elif char in closes:
                if len(stack) > 0 and stack[-1] == closes[char]:
                    stack.pop()
                else:
                    stack.append(char)

        if len(stack) != 0:
            return False
        return True
        

class TestSolution(unittest.TestCase):
    def testIsValid(self):
        solution = Solution()

        s = "()"
        expected = True
        actual = solution.isValid(s)
        self.assertEqual(expected, actual)

        s = "()[]{}"
        expected = True
        actual = solution.isValid(s)
        self.assertEqual(expected, actual)


        s = "(]"
        expected = False
        actual = solution.isValid(s)
        self.assertEqual(expected, actual)

        s = "]"
        expected = False
        actual = solution.isValid(s)
        self.assertEqual(expected, actual)

        s = "[()[]{}]"
        expected = True
        actual = solution.isValid(s)
        self.assertEqual(expected, actual)

        s = "((()))"
        expected = True
        actual = solution.isValid(s)
        self.assertEqual(expected, actual)

        s = "(((){}))"
        expected = True
        actual = solution.isValid(s)
        self.assertEqual(expected, actual)


unittest.main()