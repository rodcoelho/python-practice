"3rd Largest number in the array without sorting"

import unittest

class Solution():
    def thirdLargest(self, nums):
        largest0 = None
        largest1 = None
        largest2 = None

        for num in nums:

            # check for largest
            if largest0 is None or num > largest0:
                largest2 = largest1
                largest1 = largest0
                largest0 = num

            # check for second largest
            elif largest1 is None or largest0 > num > largest1:

                if num == largest0:
                    continue

                largest2 = largest1
                largest1 = num

            # check for third largest
            elif largest2 is None or largest1 > num > largest2:
                
                if num == largest0 or num == largest1:
                    continue

                largest2 = num

        return largest2

class TestSolution(unittest.TestCase):
    def testThirdLargest(self):
        s = Solution()

        nums = [1,3,4,6,7,3,4,8,9,10]
        expected = 8
        actual = s.thirdLargest(nums)
        self.assertEqual(actual, expected)

        nums = [9,7,6,5,2,1]
        expected = 6
        actual = s.thirdLargest(nums)
        self.assertEqual(actual, expected)

        nums = [9,9,9,9,9,9,9,9,9,9,9,9,99,1]
        expected = 1
        actual = s.thirdLargest(nums)
        self.assertEqual(actual, expected)


unittest.main()
