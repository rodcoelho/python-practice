#!/usr/bin/env python3

# Given an array of integers, find a combination of four elements in the array whose sum is equal to a given value X.

# Assume the array is less than len(100)

from itertools import combinations


def four_elements(array, value):
    for e in combinations(array, 4):
        if sum(e) == value:
            print(str(e) + ' = ' + str(sum(e)))
            return 1
    print('No four elements add up to {}'.format(str(value)))
    return 0


if __name__ == '__main__':
    assert four_elements([x for x in range(100)], 390) == 1
    assert four_elements([x for x in range(100)], 391) == 0
    assert four_elements([x for x in range(100)], 1) == 0
    assert four_elements([x for x in range(100)], 6) == 1
