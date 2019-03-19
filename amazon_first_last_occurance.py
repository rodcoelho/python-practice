#!/usr/bin/env python3

# Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

#  If the number x is not found in the array just print '-1'.

# Output: Print index of the first and last occurrences of the number x with a space in between.


def get_indexes(x, s):
    arr = s.split(' ')
    arr = [int(y) for y in arr]

    output = []
    for i in range(len(arr)):
        if arr[i] == x:
            output.append(i)

    if len(output) == 0:
        return -1
    elif len(output) == 1:
        return [output[0], output[0]]
    else:
        return [output[0], output[-1]]


if __name__ == "__main__":
    assert get_indexes(5, '1 3 5 5 5 5 67 123 125') == [2, 5], 'error1'
    assert get_indexes(7, '1 3 5 5 5 5 7 123 125') == [6, 6], 'error2'
    assert get_indexes(99, '1 3 5 5 5 5 7 123 125') == -1, 'error3'
    print("TESTS PASSED")


