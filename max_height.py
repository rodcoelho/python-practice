#!/usr/bin/env python3

# Given a struct array of type Height, having two elements feet and inches.
# Find the maximum height, where height is calculated sum of feet and inches after converting feet into inches.

# Testcase 1: (1, 2) and (2, 1) are respective given heights, i.e. [1, 2, 2, 1]
# After converting both heigths in to inches, we get 14 and 25 as respective heights.
# So, 25 is the maximum height.

def get_max(dimension):
    max = 0
    dim = [dimension[i:i+2] for i in range(0, len(dimension), 2)]
    for pair in dim:
        inches = pair[0] * 12 + pair[1]
        if inches > max:
            max = inches
    return max

if __name__ == '__main__':
    assert get_max([1, 2, 2, 1]) == 25, 'error 1'
    assert get_max([3, 5, 7, 9, 5, 6, 5, 5]) == 93, 'error 2'
    print("TESTS PASSED")
