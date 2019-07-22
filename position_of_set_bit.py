#!/usr/bin/env python3

# Given a number having only one ‘1’ and all other ’0’s in its binary representation, 
# find position of the only set bit. 
# If there is only one '1' bit then print that position else print -1. 
# Position of  set bit '1' should be counted starting with 1 from LSB side in binary 
# representation of the number.


def get_position(num):
    binary = bin(num)[2:][::-1]
    if binary.count('1') > 1:
        return -1
    return binary.find('1') + 1


if __name__ == '__main__':
    assert get_position(2) == 2, 'error 1'
    assert get_position(5) == -1, 'error 2'
    print("TESTS PASSED")
