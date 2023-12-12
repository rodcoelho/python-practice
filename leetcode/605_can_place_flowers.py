"""
You have a long flowerbed in which some of the plots are planted, and some are not. 

However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

import unittest
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):

            if flowerbed[i] == 1:
                continue
            else:
                back_index = i-1
                forward_index = i+1

                if back_index >= 0 and forward_index < len(flowerbed):
                    # middle of flowerbed
                    back = flowerbed[back_index]
                    forward = flowerbed[forward_index]
                    if back == 0 and forward == 0:
                        flowerbed[i] = 1
                        count += 1
                        continue
                elif back_index >= 0:
                    # we're at the end of flowerbed
                    back = flowerbed[back_index]
                    if back == 0:
                        flowerbed[i] = 1
                        count += 1
                        continue
                elif forward_index < len(flowerbed):
                    # we're at the beginning of flowerbed
                    forward = flowerbed[forward_index]
                    if forward == 0:
                        flowerbed[i] = 1
                        count += 1
                        continue
                else:
                    # flowerbed doesn't have before or after
                    flowerbed[i] = 1
                    count += 1
                    continue

            if count >= n:
                return True
            
        if count >= n:
            return True
            
        return False

            
class TestSolution(unittest.TestCase):
    def testCanPlaceFlowers(self):
        s = Solution()

        flowerbed = [1,0,0,0,1]
        n = 1
        expected = True
        actual = s.canPlaceFlowers(flowerbed, n)
        self.assertEqual(actual, expected)

        flowerbed = [1,0,0,0,1]
        n = 2
        expected = False
        actual = s.canPlaceFlowers(flowerbed, n)
        self.assertEqual(actual, expected)

        flowerbed = [0,0,1,0,1]
        n = 1
        expected = True
        actual = s.canPlaceFlowers(flowerbed, n)
        self.assertEqual(actual, expected)
        
        flowerbed = [1,0,0,0,0,1]
        n = 2
        expected = False
        actual = s.canPlaceFlowers(flowerbed, n)
        self.assertEqual(actual, expected)

        flowerbed = [0]
        n = 1
        expected = True
        actual = s.canPlaceFlowers(flowerbed, n)
        self.assertEqual(actual, expected)
        

unittest.main()