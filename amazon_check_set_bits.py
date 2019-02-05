#!/usr/bin/env python3

# Given a number N. Write a program to check whether every bit in the binary representation of the given number is set or not.

# Output: For each test case, return "YES" without quotes if all bits of N are set otherwise return "NO".


def get_bits_set_bool(num):
    bin_num = "{0:b}".format(num)
    bin_set = set(list(bin_num))
    print(bin_set)

    if len(bin_set) == 2:
        return "NO"
    return "YES"


if __name__ == '__main__':
    assert get_bits_set_bool(7) == 'YES', 'error1'
    assert get_bits_set_bool(14) == 'NO', 'error2'
    assert get_bits_set_bool(4) == 'NO', 'error3'
    print("TESTS PASSED")
