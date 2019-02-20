#!/usr/bin/env python3

# You are given an integer n. You need to convert all zeroes of n to 5.

# Output: The output of the function will be an integer where all zero's are converted to 5 .


def convert_five(num):
    num = list(str(num))
    num = ['5' if x == '0' else x for x in num]
    num = ''.join(num)
    print(num)
    return int(num)

if __name__ == '__main__':
    assert convert_five(1004) == 1554, 'error1'
    assert convert_five(121) == 121, 'error2'
    print("TESTS PASSED")
