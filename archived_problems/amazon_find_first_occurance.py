#!/usr/bin/env python3

# Given a sorted array consisting 0’s and 1’s. The task is to find the index of first ‘1’ in the given array.

# Output: For each test case, in a new line print the index of first 1. If 1 is not present in the array then print “-1”.


def get_index(s):
    s = s.split(' ')
    index = None
    for i in range(len(s)):
        if s[i] == '1':
            index = i
            break
    if index is None:
        return -1
    else:
        return int(index)
        


if __name__ == "__main__":
    assert get_index('0 0 0 0 0 0 1 1 1 1') == 6, 'error1'
    assert get_index('0 0 0 0') == -1, 'error2'
    print("TESTS PASSED")
