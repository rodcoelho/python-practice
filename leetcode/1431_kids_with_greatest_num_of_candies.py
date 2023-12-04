"""
There are n kids with candies. 

You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, 
where result[i] is true if, after giving the ith kid all the extraCandies, 
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""

from typing import List
import unittest

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_no_extra = 0
        for candy in candies:
            if candy > max_no_extra:
                max_no_extra = candy

        candy_bool = []
        for candy in candies:
            if candy + extraCandies >= max_no_extra:
                candy_bool.append(True)
            else:
                candy_bool.append(False)
    
        return candy_bool

class TestSolution(unittest.TestCase):
    def testKidsWithCandies(self):
        s = Solution()

        candies = [2,3,5,1,3]
        extraCandies = 3
        expected = [True,True,True,False,True] 
        actual = s.kidsWithCandies(candies, extraCandies)
        self.assertEqual(actual, expected)

        candies = [4,2,1,1,2]
        extraCandies = 1
        expected = [True,False,False,False,False] 
        actual = s.kidsWithCandies(candies, extraCandies)
        self.assertEqual(actual, expected)

        candies = [12,1,12]
        extraCandies = 10
        expected = [True,False,True]
        actual = s.kidsWithCandies(candies, extraCandies)
        self.assertEqual(actual, expected)


unittest.main()