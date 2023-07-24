#!/usr/bin/env python3

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Ex: Conisder 98, we get 9+8  = 17 after first addition. Then we get 1+7 = 8.

def rep_add_digits(num):
    if len(str(num)) == 1:
        return num
    return rep_add_digits(sum([int(x) for x in str(num)]))


if __name__ == "__main__":
    assert rep_add_digits(1) == 1, 'error 1'
    assert rep_add_digits(23) == 5, 'error 2'
    assert rep_add_digits(98) == 8, 'error 3'
    assert rep_add_digits(0) == 0, 'error 4'
    assert rep_add_digits(199) == 1, 'error 5'
    print("TESTS PASSED")
