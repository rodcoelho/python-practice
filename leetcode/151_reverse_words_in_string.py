"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.
"""

import unittest


class Solution:
    def reverseWordsPythonic(self, s:str) -> str:
        listed = [x for x in s.split(" ") if len(x) > 0]
        s = " ".join(listed[::-1])
        return s
    
    def reverseWords(self, s: str) -> str:
        final = ""
        beg_word = False
        temp = ""

        for i in range(len(s)):

            current = s[i]

            # new word begins
            if current != " " and beg_word is False:
                beg_word = True
                temp += current

            # middle of word
            elif current != " " and beg_word is True:
                temp += current
                
            # word ends
            elif current == " " and beg_word is True:
                if final == "":
                    final = temp
                else:
                    final = temp + " " + final
                temp = ""
                beg_word = False
                
            # just a space
            elif current == " " and beg_word is False:
                continue

        # catch last words
        if temp != "":
            if final == "":
                final = temp
            else:
                final = temp + " " + final

        return final
            

class TestSolution(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()

        s = "the sky is blue"
        expected = "blue is sky the"
        actual = solution.reverseWords(s)
        self.assertEqual(actual, expected)
        
        s = "  hello world  "
        expected = "world hello"
        actual = solution.reverseWords(s)
        self.assertEqual(actual, expected)
        
        s = "a good   example"
        expected = "example good a"
        actual = solution.reverseWords(s)
        self.assertEqual(actual, expected)

        s = " example "
        expected = "example"
        actual = solution.reverseWords(s)
        self.assertEqual(actual, expected)

    def test_reverse_pythonic(self):
        solution = Solution()

        s = "the sky is blue"
        expected = "blue is sky the"
        actual = solution.reverseWordsPythonic(s)
        self.assertEqual(actual, expected)

        s = "  hello world  "
        expected = "world hello"
        actual = solution.reverseWordsPythonic(s)
        self.assertEqual(actual, expected)

        s = "a good   example"
        expected = "example good a"
        actual = solution.reverseWordsPythonic(s)
        self.assertEqual(actual, expected)

        s = " example "
        expected = "example"
        actual = solution.reverseWordsPythonic(s)
        self.assertEqual(actual, expected)


unittest.main()