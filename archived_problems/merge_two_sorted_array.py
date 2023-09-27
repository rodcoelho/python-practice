#!/usr/bin/env python3

import unittest


class SortedArrayMerger:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2
        self.final = []

    def merge(self):
        for i in range(len(self.array1) + len(self.array2)):
            head1 = self.array1[0] if self.array1 else None
            head2 = self.array2[0] if self.array2 else None

            if head2 is not None:
                if head1 is None or head1 > head2:
                    self.final.append(head2)
                    self.array2 = self.array2[1:]
                    continue
            if head1 is not None:
                if head2 is None or head1 < head2:
                    self.final.append(head1)
                    self.array1 = self.array1[1:]
                    continue
            
        return self.final

    
class SortedArrayMergerInPlace:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def merge(self):
        last_checked = 0

        for i in range(len(self.array2)):
            current_pop = self.array2[0]
            self.array2 = self.array2[1:]

            if len(self.array1) == 0:
                self.array1= [current_pop]
                continue

            altered = False
            while not altered:

                try: 
                    if self.array1[last_checked] < current_pop < self.array1[last_checked+1]:
                        self.array1 = self.array1[:last_checked + 1] + [current_pop] + self.array1[last_checked+1:]
                        altered = True
                except:
                    if self.array1[last_checked] < current_pop:
                        self.array1 = self.array1[:last_checked + 1] + [current_pop]
                        altered = True    

                last_checked += 1

        return self.array1


class TestSortedArrayMerger(unittest.TestCase):
    def test_SortedArrayMerger_merge(self):
        array1 = [1,3,7,8,9]
        array2 = [2,4,5,6,10]
        expected = [1,2,3,4,5,6,7,8,9,10]
        am = SortedArrayMerger(array1, array2)
        actual = am.merge()
        self.assertEqual(actual, expected)
    
    def test_SortedArrayMerger_merge_2(self):
        array1 = [1,3,5,6,7,8,9,10]
        array2 = [2,4]
        expected = [1,2,3,4,5,6,7,8,9,10]
        am = SortedArrayMerger(array1, array2)
        actual = am.merge()
        self.assertEqual(actual, expected)

    
    def test_SortedArrayMerger_merge_3(self):
        array1 = [1,3]
        array2 = [2,4,5,6,7,8,9,10]
        expected = [1,2,3,4,5,6,7,8,9,10]
        am = SortedArrayMerger(array1, array2)
        actual = am.merge()
        self.assertEqual(actual, expected)


    def test_SortedArrayMerger_merge_4(self):
        array1 = []
        array2 = [1,2,3,4,5,6,7,8,9,10]
        expected = [1,2,3,4,5,6,7,8,9,10]
        am = SortedArrayMerger(array1, array2)
        actual = am.merge()
        self.assertEqual(actual, expected)


class TestSortedArrayMergerInPlace(unittest.TestCase):
    def test_SortedArrayMergerInPlace_merge(self):
        array1 = [1,3,7,8,9]
        array2 = [2,4,5,6,10]
        expected = [1,2,3,4,5,6,7,8,9,10]
        am = SortedArrayMergerInPlace(array1, array2)
        actual = am.merge()
        self.assertEqual(actual, expected)
    
    def test_SortedArrayMergerInPlace_merge_2(self):
        array1 = [1,3,5,6,7,8,9,10]
        array2 = [2,4]
        expected = [1,2,3,4,5,6,7,8,9,10]
        am = SortedArrayMergerInPlace(array1, array2)
        actual = am.merge()
        self.assertEqual(actual, expected)
    
    def test_SortedArrayMergerInPlace_merge_3(self):
        array1 = [1,3]
        array2 = [2,4,5,6,7,8,9,10]
        expected = [1,2,3,4,5,6,7,8,9,10]
        am = SortedArrayMergerInPlace(array1, array2)
        actual = am.merge()
        self.assertEqual(actual, expected)

    def test_SortedArrayMergerInPlace_merge_4(self):
        array1 = []
        array2 = [1,2,3,4,5,6,7,8,9,10]
        expected = [1,2,3,4,5,6,7,8,9,10]
        am = SortedArrayMergerInPlace(array1, array2)
        actual = am.merge()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()