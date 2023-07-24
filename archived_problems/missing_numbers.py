#!/usr/bin/env python3

# you are given an array of values that either count


def find_missing_num(arr):
    answer = None
    skip = find_skip(arr)
    if skip is not False:
        for i in range(0, len(arr) - 1):
            if arr[i] + skip != arr[i + 1]:
                answer = arr[i] + skip
        return answer


def find_skip(arr):
    skip = arr[1] - arr[0]
    skip2 = arr[-1] - arr[-2]
    if skip == skip2:
        return skip
    else:
        skip = arr[-2] - arr[-3]
        skip2 = arr[2] - arr[1]
        if skip == skip2:
            return skip
    return False


def best_case(arr):
    gap = None
    for i in range(0, len(arr)-1):
        temp_gap = abs(arr[i+1] - arr[i])
        if gap is None:
            gap = temp_gap
        else:
            if temp_gap > gap:
                # if descending
                if arr[i] > arr[i+1]:
                    return arr[i] - gap
                # if ascending
                return arr[i] + gap
            elif gap > temp_gap:
                # if descending
                if arr[i] > arr[i+1]:
                    return arr[i] + temp_gap
                # if ascending
                return arr[i] - temp_gap


if __name__ == '__main__':
    assert find_missing_num([2, 6, 8, 10]) == 4, 'error1'
    assert best_case([2, 6, 8, 10]) == 4, 'error2'
    assert best_case([10, 8, 4, 2]) == 6, 'error3'


# works for worst case big O of N
# improve code to improve the best case scenario

