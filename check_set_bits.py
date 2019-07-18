#!/usr/bin/env python3

# Given a number N. Write a program to check whether every bit in the
# binary representation of the given number is set or not.


def check_set_bit(num):
    bit = bin(num)[2:]
    if '0' in bit:
        return False
    return True

if __name__ == "__main__":
    assert check_set_bit(7) == True, 'error 1'
    assert check_set_bit(14) == False, 'error 2'
    assert check_set_bit(4) == False, 'error 3'
    assert check_set_bit(0) == False, 'error 4'
    assert check_set_bit(1) == True, 'error 5'
    print("TESTS PASSED")
