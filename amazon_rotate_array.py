#!/usr/bin/env python3

# Given an array of size N, rotate it by D elements. 

# Input: 
# The first line of the input contains T denoting the number of testcases. First line of test case is the number of elements N, next line contains D. Subsequent line will be the array elements.

# Output: 
# For each testcase, in a new line, output the rotated array.


def rotate_array(arr, shift):
    return arr[shift:] + arr[:shift]


if __name__ == "__main__":
    print("BEGIN TESTS")
    assert rotate_array([1,2,3,4,5], 2) == [3,4,5,1,2], 'error1'
    assert rotate_array([2,4,6,8,10,12,14,16,18,20], 3) == [8,10,12,14,16,18,20,2,4,6], 'error2'
    print("TESTS PASSED")
