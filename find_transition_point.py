#!/usr/bin/env python3

# You are given a sorted array containing only numbers 0 and 1.
# Find the transition point efficiently. Transition point is a 
# point where "0" ends and "1" begins.


def get_transition(arr):
    return len(arr) - sum(arr)


if __name__ == "__main__":
    assert get_transition([0, 0, 0, 1, 1]) == 3, 'test 1'
    assert get_transition([0, 1, 1, 1, 1]) == 1, 'test 2'
    assert get_transition([1, 1, 1, 1, 1]) == 0, 'test 3'
    print("TESTS PASSED")

