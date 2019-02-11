#!/usr/bin/env python3

# You are given two numbers X and Y. Write a program to count number of bits needed to be flipped to convert X to Y.

# Output: Print the number of bits needed to be flipped.


def get_bits_flip(x, y):
    count = 0
    x = list("{0:b}".format(x))
    y = list("{0:b}".format(y))
    xzero = [0] * (8 - len(x))
    yzero = [0] * (8 - len(y))
    x = xzero + x
    y = yzero + y
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1

    print(count)
    return count


if __name__ == '__main__':
    assert get_bits_flip(10, 20) == 4, 'error1'
    print("TESTS PASSED")
