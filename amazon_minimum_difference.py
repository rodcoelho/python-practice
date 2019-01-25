#!/usr/bin/env python3

# Given an unsorted array, find the minimum difference between any pair in given array.

# Input:

# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is N, the size of array. Second line of the test case is the Array.

# Output:

# Print the minimum difference between any two pairs.


def get_min_diff(arr):
    min = None
    arr.sort()
    for i in range(len(arr) - 1):
        diff = arr[i] - arr[i+1]
        diff = abs(diff)
        if min is None:
            min = diff
        else:
            if diff < min:
                min = diff
    return min


if __name__ == "__main__":
    assert get_min_diff([2,4,5,7,9]) == 1, 'error 1'
    assert get_min_diff([87, 32, 99, 75, 56, 43, 21, 10, 68, 49]) == 6, 'error2'
    print("TESTS PASSED")
