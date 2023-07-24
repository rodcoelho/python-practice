#!/usr/bin/env python3

# Given a number N. The task is to generate a list of  all binary numbers with decimal values from 1 to N.

def get_bin_list(num):
    bins = []
    for i in range(1, num + 1):
        bins.append(int(bin(i)[2:]))
    return bins


if __name__ == "__main__":
    assert get_bin_list(2) == [1, 10], 'error 1'
    assert get_bin_list(5) == [1, 10, 11, 100, 101], 'error 2'
    print("TESTS PASSED")
