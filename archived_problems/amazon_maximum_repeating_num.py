#!/usr/bin/env python3

# Given an array A of size N, the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= N. Find the maximum repeating number in this array. If there are two or more maximum repeating numbers print the element having least value.

# Output: For each testcase, in a new line, print the maximum frequency element.


def get_max_reps(s):
    arr = s.split(' ')
    arr = [int(x) for x in arr]
    
    maxx = {}

    for ele in arr:
        if arr.count(ele) > 1:
            if arr.count(ele) in maxx:
                maxx[arr.count(ele)].append(ele)
            else:
                maxx[arr.count(ele)] = [ele]

    if len(maxx) == 0:
        return -1
    
    max_count = max(maxx.keys())
    maxx = maxx[max_count]

    return min(maxx)
    


if __name__ == "__main__":
    assert get_max_reps("2 2 1 2") == 2, 'error1'
    assert get_max_reps("2 2 1 0 0 1") == 0, 'error2'
    assert get_max_reps("1 2 3") == -1, 'error3'
    print("TESTS PASSED")
