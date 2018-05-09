#!/usr/bin/env python3


def missing_kth_element(arr, k):
    ideal = [x for x in range(arr[0], arr[-1])]
    for i in range(len(arr)):
        if arr[i] in ideal:
            ideal.remove(arr[i])
    try:
        return ideal[k-1]
    except:
        return -1


if __name__ == '__main__':
    assert missing_kth_element([1, 3, 5, 7, 9, 11], 2) == 4, 'error 1' # should return 4
    assert missing_kth_element([1, 2, 3, 4, 5, 7], 2) == -1, 'error 2' # should throw error -1
    assert missing_kth_element([1, 2, 3, 4, 5, 6], 3) == -1, 'error 3' # should throw error -1
    assert missing_kth_element([1, 2], 4), 'error 4'                   # should throw error -1

