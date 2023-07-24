#!/usr/bin/env python3

# Given a positive integer n, find if it can be expressed as x^y where y > 1 and x > 0 and x and y both are both integers.

# Output: For each test case in a new line print 1 if the number can be expressed as  xy else print 0.


def get_xy(n):
    if n < 1:
        return 0
    x_gen = [x for x in range(1,n)]
    y_gen = [x for x in range(2,n)]

    for x in x_gen:
        for y in y_gen:
            if x**y == n:
                return 1

    return 0


if __name__ == '__main__':
    assert get_xy(8) == 1, 'error1'
    assert get_xy(5) == 0, 'error2'
    assert get_xy(-4) == 0, 'error3'
    print("TESTS PASSED")
