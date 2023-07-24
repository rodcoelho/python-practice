#!/usr/bin/env python3

# Given an integer X within the range of 0 to 9, and given two positive integers as upper and lower bounds respectively, find the number of times X occurs as a digit in an integer within the range, excluding the bounds. Print the frequency of occurrence as output.

# Input:
# The first line of input is an integer T, denoting the number of test cases. For each test case, there are two lines of input, first consisting of the integer X, whose occurrence has to be counted. Second, the lower and upper bound, L and U which are positive integers, on the same line separated by a single space, respectively.

# Output:
# For each test case, there is only one line of output, the count of the occurrence of X as a digit in the numbers lying between the lower and upper bound, excluding them.


def find_how_many_x(digit, lower, upper):
    count = 0
    for i in range(lower + 1, upper):
        for ele in list(str(i)): 
            if str(digit) == ele:
                count += 1
    return count


if __name__ == '__main__':
    print("TESTS BEGIN")
    assert find_how_many_x(3, 100, 250) == 35, 'error 1'
    assert find_how_many_x(2, 10000, 12345) == 1120, 'error 2'
    assert find_how_many_x(0, 20, 21) == 0, 'error 3'
    assert find_how_many_x(9, 899, 1000) == 120, 'error 4'
    assert find_how_many_x(1, 1100, 1345) == 398, 'error 5'
    print("ALL TESTS PASS")
