#!/usr/bin/env python3

import itertools

# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

# Output: For each testcase, print True or False


def bool_py_triplet(s):
    arr = s.split(" ")
    arr = [int(x) for x in arr]
    c2 = {}
    for i in range(len(arr)):
        c2[arr[i]*arr[i]] = arr[i]

    found = False
    
    combos = []
    for comb in itertools.combinations(arr,2):
        combos.append(comb)

    for comb in combos:
        if comb[0] * comb[0] + comb[1] * comb[1] in c2:
            possible_match = c2[comb[0] * comb[0] + comb[1] * comb[1]]
            if possible_match not in comb:
                found = True
                print("{a}^2 + {b}^2 = {c}^2".format(a=comb[0], b=comb[1], c=possible_match))

    return found


if __name__ == "__main__":
    assert bool_py_triplet("3 2 4 6 5") == True, 'error1'
    print("TESTS PASSED")
