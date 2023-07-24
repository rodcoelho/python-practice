#!/usr/bin/env python3

# Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

# Output: For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.


def get_majority(s):
    arr = s.split(" ")
    arr = [int(x) for x in arr]
    threshold = len(arr) / 2

    max = {}
    max_count = 1

    for i in range(len(arr)):
        if arr.count(arr[i]) > threshold:
            if arr.count(arr[i]) > max_count:
                max[arr.count(arr[i])] = arr[i]
                max_count = arr.count(arr[i])
                       
    if max_count == 1:
        return "-1"
    else:
        return str(max[max_count])


if __name__ == "__main__":
    assert get_majority("3 1 3 3 2") == "3", 'error1'
    assert get_majority("1 2 3") == "-1", 'error2'
    print("TESTS PASSED")
