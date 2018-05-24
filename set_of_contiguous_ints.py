#!/usr/bin/env python3

# Given an array of n integers(duplicates allowed). Print “Yes” if it is a set of contiguous integers else print “No”.


def set_of_contiguous_ints(l_ints):
    valid = True
    # get set from list
    s_ints = list(set(l_ints))
    for i in range(len(s_ints)-1):
        if s_ints[i] + 1 != s_ints[i+1]:
            valid = False
    if valid:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    assert set_of_contiguous_ints([5, 2, 3, 6, 4, 4, 6, 6]) == "Yes", 'error1'
    assert set_of_contiguous_ints([10, 14, 10, 12, 12, 13, 15]) == "No", 'error2'

