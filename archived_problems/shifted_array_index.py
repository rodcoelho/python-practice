#!/usr/bin/env python3

# find a number in the array

shifted_array = [5, 6, 7, 8, 9, 1, 2, 3, 4]

cache = {}


def create_cache(arr):
    for i in range(len(arr)):
        cache[arr[i]] = i


def find_index(arr, num):
    create_cache(arr) # BigO N
    if not cache or num not in cache:
        return -1
    else:
        return cache[num] # BigO 1


x = find_index(shifted_array, 99)
print(x)


y = find_index(shifted_array, 9)
print(y)

