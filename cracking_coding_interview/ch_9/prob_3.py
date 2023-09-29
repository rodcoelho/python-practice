# Given a sorted array of n integers that has been rotated an unknown number of times, 
# give an O(log n) algorithm that finds an element in the array.
# You may assume that the array was originally sorted in increasing order.

import unittest

class ElementFinder:
    def __init__(self, array):
        self.array = array

    def find(self, target):
        first, last = 0, len(self.array) -1
        print("__________________", target)
        return self.bst(first, last, target)

    def bst(self, beg, end, target):
        mid = (end + beg) // 2
        print(beg, mid, end, target)
        if self.array[mid] == target:
            return mid
        elif self.array[mid-1] == target:
            return mid-1
        elif self.array[beg] == target:
            return beg
        elif self.array[end] == target:
            return end

        # check left 
        # [option1: ordered properly, beg --> target --> mid] 
        # [option2: not ordered properly, beg --> mid --> target]
        # [option3: not ordered properly, target --> beg --> mid]
        if (self.array[beg] < self.array[mid] and target <= self.array[mid-1] and target >= self.array[beg]) or \
        (self.array[beg] > self.array[mid-1] and target >= self.array[beg] and target >= self.array[mid-1]) or \
        (self.array[beg] > self.array[mid-1] and target <= self.array[beg] and target <= self.array[mid-1]):
            print("RETURN LEFT", beg, mid, target)
            return self.bst(beg, mid, target)
        else:
            print("RETURN RIGHT", mid, end, target)
            return self.bst(mid, end, target)


class TestElementFinder(unittest.TestCase):        
    def test_find(self):
        test_cases = [
            [9,10,11,1,2,  3,    4,5,6,7,8],   # odd, left shift
            [5,6,7,8,      9,    10,1,2,3],    # odd, right shift
            [1,2,3,5,      6,    7,8,9,10],    # odd, no shift
            [7,8,9,10,           1,2,3,5],     # even, no shift
            [3,5,7,8,            9,10,1,2],    # even, right shift
            [10,1,2,3,           5,7,8,9],     # even, left shift
        ]
        for test_case in test_cases:
            ef = ElementFinder(test_case)
            for i in range(len(test_case)):

                case = test_case[i]
                expected = i
                
                print(case, expected)

                actual = ef.find(case)
                
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
