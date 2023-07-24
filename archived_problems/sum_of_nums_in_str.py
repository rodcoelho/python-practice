#!/usr/bin/env python3

# Sum of numbers in string

# Given a string str containing alphanumeric characters, calculate sum of all numbers present in the string.

# Ex: '1abc23' ==> 24

def total_sum(s):
    nums = ''
    for char in s:
        try:
            float(char)
            nums += char
        except ValueError:
            nums += ','
    nums = [int(num) for num in nums.split(',') if num]
    return sum(nums)
    

if __name__ == '__main__':
    assert total_sum('1abc23') == 24, 'test 1'
    assert total_sum('geeks4geeks') == 4, 'test 2'
    assert total_sum('1abc2x30yz67') == 100, 'test 3'
    assert total_sum('123abc') == 123, 'test 4'
    assert total_sum('abc') == 0, 'test 5'
    print("TESTS PASSED")

