#!/usr/bin/env python3

# Given an integer X within the range of 0 to 9, and given two positive integers as upper and lower bounds respectively, find the number of times X occurs as a digit in an integer within the range, excluding the bounds. Print the frequency of occurrence as output.


def find_x_in_range(x, lower, upper):
    count = 0
    gen_x = (y for y in range(lower+1, upper))
    for e in gen_x:
        e = str(e)
        for char in e:
            if char == str(x):
                count += 1
    return count

if __name__ == '__main__':
    assert find_x_in_range(3, 100, 250) == 35
    assert find_x_in_range(2, 10000, 12345) == 1120
    assert find_x_in_range(0, 20, 21) == 0
    assert find_x_in_range(9, 899, 1000) == 120
    assert find_x_in_range(1, 1100, 1345) == 398

