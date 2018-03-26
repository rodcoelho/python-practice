# Given an array of unsorted positive integers,
# write a function # that finds runs of 3 consecutive
# numbers (ascending or descending) and returns the
# indices where such runs begin. If no such runs are
# found, return null.

# function findConsecutiveRuns(input:Array):Array
# Example:  [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7]
# would return [0, 4, 6, 7]

# Please build a minimal Python unittest suite for
# your function.  Once you have completed the exercise,
# we will schedule a call where we will go over and
# work with your code live.

import unittest

given_example = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7]
ex1 = [x for x in range(10)]
ex2 = ex1[::-1]
ex3 = ex1[0::2]
ex4 = [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]
ex5 = [1, 2, 3, 2, 1]


def find_consecutive_runs(input_array):
    payload = []

    for i in range(0, len(input_array)):
        try:
            # check if ascending
            if input_array[i] == input_array[i + 1] + 1:
                if input_array[i] == input_array[i + 2] + 2:
                    payload.append(i)
        except:
            pass
    for i in range(0, len(input_array)):
        try:
            # check if descending
            if input_array[i] == input_array[i + 1] - 1:
                if input_array[i] == input_array[i + 2] - 2:
                    payload.append(i)
        except:
            pass
    if not payload:
        return [0]
    else:
        return sorted(payload)


class TestThis(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_consecutive_runs([0, 1, 2]), [0])

    def test_given(self):
        self.assertEqual(find_consecutive_runs(given_example), [0, 4, 6, 7])

    def ex1_test(self):
        self.assertEqual(find_consecutive_runs(ex1), [0, 1, 2, 3, 4, 5, 6, 7])

    def ex2_test(self):
        self.assertEqual(find_consecutive_runs(ex2), [0, 1, 2, 3, 4, 5, 6, 7])

    def ex3_test(self):
        self.assertEqual(find_consecutive_runs(ex3), [0])

    def ex4_test(self):
        self.assertEqual(find_consecutive_runs(ex4), [0, 13])

    def ex5_test(self):
        self.assertEqual(find_consecutive_runs(ex5), [0, 2])


unittest.main()

