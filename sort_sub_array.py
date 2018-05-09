#!/usr/bin/env/ python3

# Given an array A[N], you are required to sort the array in given index range [a, b], i.e., you need to sort subarray A[a..b]


def my_sort(arr):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                unsorted = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def sort_sub_array(arr, a, b):
    return arr[:a] + my_sort(arr[a:b]) + arr[b:]


if __name__ == '__main__':
    x = sort_sub_array([9, 8, 7, 6, 5, 3, 2, 1, 0], 3, 6)
    print(x)

