#!/usr/bin/env python3


# Given street of houses (a row of houses), each house having some amount of money kept inside; now there is a thief who is going to steal this money but he has a constraint/rule that he cannot steal/rob two adjacent houses. Find the maximum money he can rob.

# Input:

# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is N and money.

# Output:

# Print maximum money he can rob.


def find_maximum_money(num_of_houses, money):
    half_round_up = num_of_houses / 2.0
    if half_round_up.is_integer():
        return int(half_round_up) * money
    else:
        half_round_up = str(half_round_up).split('.')[0]
        half_round_up = int(half_round_up) + 1
        return half_round_up * money


if __name__ == '__main__':
    print("BEGINNING TESTS")
    assert find_maximum_money(5, 10) == 30, 'error 1'
    assert find_maximum_money(2, 12) == 12, 'error 2'
    print("TESTS PASSED")
