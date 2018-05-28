#!/usr/bin/env python3

# you are given an array of values that either count


def missing_number(arr):
    answer = -1

    for i in range(0, len(arr)-1):
        if arr[i] + 1 == arr[i + 1]:
            pass
        else:
            answer = arr[i] + 1

    return answer


if __name__ == '__main__':
    assert missing_number([1, 2, 3, 5, 6, 7]) == 4, 'error1'

# next we want to be able to do it for skips
# then we want to be able to do it counting down


