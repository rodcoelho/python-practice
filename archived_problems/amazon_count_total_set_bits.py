#!/usr/bin/env python3

  
# Find the sum of all bits from numbers 1 to N.

# Input: N

# Output: Print the sum of all bits.


def get_sum_of_bits(num):
    sum = 0
    for i in range(num + 1):
        bit = "{0:b}".format(i).count('1')
        sum += bit
    print(sum)
    return sum
        


if __name__ == '__main__':
    assert get_sum_of_bits(4) == 5, 'error1'
    assert get_sum_of_bits(17) == 35, 'error2'
    print("PASSED ALL TESTS")
