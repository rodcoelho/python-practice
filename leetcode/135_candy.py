"""
There are n children standing in a line. 
Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""

import unittest
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for x in ratings]

        # left_to_right
        prior = ratings[0]
        for i in range(1,len(ratings)):
            if ratings[i] > prior:

                candies[i] = candies[i-1] + 1
            prior = ratings[i]

        # right to left
        prior = ratings[-1]
        for i in range(len(ratings)):
            current_i = len(ratings) - i - 1
            if ratings[current_i] > prior:
                if current_i - 1 >= 0 and ratings[current_i] > ratings[current_i - 1] and ratings[current_i] != ratings[current_i - 1]:
                    pass
                else:
                    candies[current_i] = candies[current_i+1] + 1
            prior = ratings[current_i]
        
        return sum(candies)
        

class TestSolution(unittest.TestCase):
    def test_candy(self):
        s = Solution()

        ratings = [1,0,2]
        expected = 5
        actual = s.candy(ratings)
        self.assertEqual(actual, expected)

        ratings = [1,2,2]
        expected = 4
        actual = s.candy(ratings)
        self.assertEqual(actual, expected)

        ratings = [1,3,2,2,1]
        expected = 7
        actual = s.candy(ratings)
        self.assertEqual(actual, expected)

        ratings = [1,2,87,87,87,2,1]
        expected = 13
        actual = s.candy(ratings)
        self.assertEqual(actual, expected)


unittest.main()