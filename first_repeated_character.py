#!/usr/bin/env python3

# Given a string - "str", find the repeated character 
# present first in the string.


def get_first_rep(s):
    for char in s:
        if s.count(char) > 1:
            return char
    return -1


if __name__ == "__main__":
    assert get_first_rep("hello") == 'l', 'test 1'
    assert get_first_rep("fg") == -1, 'test 2'
    assert get_first_rep("geeksforgeeks") == 'g', 'test 3'
    print("TESTS PASSED")
