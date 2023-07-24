#!/usr/bin/env python3

# Given an array with all elements greater than or equal to zero. Return the maximum product of two numbers possible.

# Output: Print the maximum product of two numbers possible.


def get_max_prod(arr):
    sorted_arr = arr.sort()
    return arr[-1] * arr[-2]


if __name__ == "__main__":
    assert get_max_prod([1, 100, 42, 4, 23]) == 4200, 'error1'
    assert get_max_prod([0, 1, 100, 3, 7]) == 700, 'error2'
    print("TESTS PASSED")
