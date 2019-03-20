#!/usr/bin/env python3

# Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

# Output: Print the missing number in array.


def get_missing(s):
    arr = s.split(" ")
    arr = [int(x) for x in arr]

    for i in range(arr[0], arr[-1]):
        if i not in arr:
            return i


if __name__ == "__main__":
    assert get_missing('1 2 3 5') == 4, 'error1'
    assert get_missing('1 2 3 4 5 6 7 8 10') == 9, 'error2'
    assert get_missing('3 4 5 6 7 8 10') == 9, 'error3'
    print("TESTS PASSED")
