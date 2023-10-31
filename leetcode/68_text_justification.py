"""
Given an array of strings words and a width maxWidth, 
format the text such that each line has exactly maxWidth characters 
and is fully (left and right) justified.

You should pack your words in a greedy approach; 
that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
"""

import unittest
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        final = []

        count = 0
        temp = ""
        temp_list = []
        while count < len(words):

            # get current word
            current = words[count]
            
            # check if temp can add current
            # add 1 to it to take into account a space needed for seperation
            if len(temp) + len(current) + 1 <= maxWidth:
                can_add_current = True
            else:
                can_add_current = False

            # if we can add current to the temp, let's do it
            if can_add_current:
                if temp == "":
                    temp = current
                else:
                    temp = temp + " " + current
                temp_list.append(current)
            # can't add current word to temp, so let's process the temp and make the current the new temp
            else:
                # calculate spaces needed to make maxWidth with temp
                # justified_temp_list is where everything will land
                justified_temp_list = ""
                spaces_needed = maxWidth - len("".join(temp_list))

                if len(temp_list) == 1:
                    # if there is one word, let's justified left
                    temp_list_with_spaces = temp_list[0] + (spaces_needed * " ")
                else:
                    # multiple words, justify to middle
                    temp_list_with_spaces = []

                    # calculate spaces between each word, rounded up
                    spaces_per = int(spaces_needed / (len(temp_list)-1 )) + (spaces_needed % (len(temp_list)-1 ) > 0)
                    
                    space_counter = 0
                    while spaces_needed > 0:
                        # add indexed word to temp
                        temp_list_with_spaces.append(temp_list[space_counter])

                        # remove spaces_per from total spaces needed
                        spaces_needed -= spaces_per
                        if spaces_needed >= 0:
                            current_spaces_per = spaces_per
                        else:
                            current_spaces_per = spaces_per + spaces_needed

                        # add spaces required after each word
                        current_spaces_per = current_spaces_per * " "
                        temp_list_with_spaces.append(current_spaces_per)
                        
                        # counter (index)
                        space_counter += 1

                    # add in the final word
                    temp_list_with_spaces.append(temp_list[-1])

                # add justified phrase to final
                final.append("".join(temp_list_with_spaces))

                # add current word that didn't fit into last batch 
                temp_list = [current]
                temp = current

            count += 1

            # get any left overs, justify left
            if count == len(words):
                temp_justify_left = " ".join(temp_list)
                spaces_left = maxWidth - len(temp_justify_left)
                temp_justify_left += " " * spaces_left
                final.append(temp_justify_left)

        return final


class TestSolution(unittest.TestCase):
    def test_justifier(self):
        s = Solution()

        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        actual = s.fullJustify(words, maxWidth)
        self.assertEqual(actual, expected)

        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        actual = s.fullJustify(words, maxWidth)
        self.assertEqual(actual, expected)

        words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        actual = s.fullJustify(words, maxWidth)
        self.assertEqual(actual, expected)

unittest.main()
