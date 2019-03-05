#!/usr/bin/env python3

# Given an array of positive integers where all numbers occur even number of times except one number which occurs odd number of times. Find the number.

# Output: Corresponding to each test case, print the number which occur odd number of times. If no such element exists, print 0.


def find_odd_count(arr):
    odds = []
    arr = arr.split(" ")
    
    for ele in arr:
        if arr.count(ele) % 2 != 0:
            odds.append(ele)

    odds = list(set(odds))

    if len(odds) == 0:
        return 0
    else:
        return int(odds[0])


if __name__ == '__main__':
    assert find_odd_count('8 4 4 8 23') == 23, 'error1'
    assert find_odd_count('1 1 1 2 2') == 1, 'error2'
    assert find_odd_count('1 1') == 0, 'error3'
    print("TESTS PASSED")
