#!/usr/bin/env python3

# Given an array containing equal number of positive and negative elements, arrange the array such that every positive element is followed by a negative element.

def rearrange_arr(arr):
    arr = arr.split(' ')
    arr = [int(x) for x in arr]

    pos = True

    for i in range(len(arr) - 1):
        if pos:
            pos = False
            if arr[i] < 0:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            pos = True
            if arr[i] > 0:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    arr = [str(x) for x in arr]
    return ' '.join(arr)


if __name__ == "__main__":
    assert rearrange_arr("-1 2 -3 4 -5 6") == "2 -1 4 -3 6 -5", 'error1'
    assert rearrange_arr("-3 2 -4 1") == "2 -3 1 -4", 'error2'
    print("TESTS PASSED")
