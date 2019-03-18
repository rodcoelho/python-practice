#!/usr/bin/env python3

import itertools

# Given an unsorted array of positive integers. Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles. 

# Output: Number of possible triangles are displayed to the user.


def get_triangles(s):
    count = 0
    arr = s.split(" ")
    arr = [int(x) for x in arr]

    for comb in itertools.combinations(arr,3):
        count += 1

    return count


if __name__ == "__main__":
    assert get_triangles("3 4 5") == 1, 'error1'
    assert get_triangles("6 4 9 7 8") == 10, 'error2'
    print("TESTS PASSED")
