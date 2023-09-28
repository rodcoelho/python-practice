#!/usr/bin/env python3

# Write a method to sort an array of strings so that all the anagrams are next to each other.

import unittest

class SortAnagram:
    def __init__(self, anagrams):
        self.anagrams = anagrams

    def sort(self):
        anagram_dict = {}
        for word in self.anagrams:
            sorted_word = "".join(sorted([char for char in word]))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
            
        self.anagrams = []
        for key, val in anagram_dict.items():
            for v in val:
                self.anagrams.append(v)
        return self.anagrams


class TestSortAnagram(unittest.TestCase):
    def test_sort(self):
        expected = ["axyz","zyxa","evil","live","kcuf","fuck"]
        array = ["axyz","evil","live","kcuf","zyxa", "fuck"]

        sa = SortAnagram(array)
        sa.sort()
        self.assertEqual(sa.anagrams, expected)


if __name__ == "__main__":
    unittest.main()
