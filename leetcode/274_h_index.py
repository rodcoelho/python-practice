"""
Given an array of integers citations where citations[i] is the number of citations 
a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: 
The h-index is defined as the maximum value of h such that the given researcher 
has published at least h papers that have each been cited at least h times.
"""

import unittest
from typing import List

class Solution:
    def h_index(self, citations: List[int]) -> int:
        
        h_count = 0
        h = 0
        
        for i in range(len(citations)):
            
            current = citations[i]
            if current == 0:
                continue

            greater_than_current = len([x for x in citations if x>= current])
            # if len of elements greater than current are more than the current value
            if greater_than_current >= current:
                # if current is greater than the prior found h
                if current > h:
                    h_count = greater_than_current
                    h = current
        return h 
            

class TestSolution(unittest.TestCase):
    def test_(self):
        s = Solution()

        citations = [3,0,6,1,5]
        expected = 3
        actual = s.h_index(citations)
        self.assertEqual(actual, expected)

        citations = [1,3,1]
        expected = 1
        actual = s.h_index(citations)
        self.assertEqual(actual, expected)

        citations = [1,3,1,2,2,2,3,5,6]
        expected = 3
        actual = s.h_index(citations)
        self.assertEqual(actual, expected)

        citations = [0,0,0,0,10,1,1,2,10,0,0,0]
        expected = 2
        actual = s.h_index(citations)
        self.assertEqual(actual, expected)


unittest.main()