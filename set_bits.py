#!/usr/bin/env python3

# Given a positive integer N, print count of set bits in it.
# Ex: if the given number is 6(binary: 110), output should be 2 as there are two set bits in it.


def get_bits(num):
    bits = bin(num)[2:]
    return bits.count('1')


if __name__ == "__main__":
    assert get_bits(6) == 2, 'error 1'
    assert get_bits(11) == 3, 'error 2'
    assert get_bits(0) == 0, 'error 3'
    assert get_bits(999) == 8, 'error 4'
    print("TESTS PASSED")
