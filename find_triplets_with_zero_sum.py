#!/usr/bin/env python3

# Given an array A[] of N elements. 
# The task is to complete the function which returns 
# true if triplets exists in array A whose sum 
# is zero else returns false.

from itertools import combinations

def has_zero(arr):
    combs = list(combinations(arr, 3))
    for comb in combs:
        if sum(comb) == 0:
            return True
    return False


if __name__ == "__main__":
    assert has_zero([0, -1, 2, -3, 1]) == True, 'test 1'
    assert has_zero([1, 2, 3]) == False, 'test 2'
    print("TESTS PASSED")


