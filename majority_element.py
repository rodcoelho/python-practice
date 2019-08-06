#!/usr/bin/env python3

# Given an array A of N elements. Find the majority element in the array. 
# A majority element in an array A of size N is an element that appears 
# more than N/2 times in the array.


def get_majority(nums):
    for num in nums:
        if nums.count(num) > len(nums)/2:
            return num
    return -1


if __name__ == "__main__":
    assert get_majority([3, 1, 3, 3, 2]) == 3, 'test 1'
    assert get_majority([1, 2, 3]) == -1, 'test 2'
    assert get_majority([]) == -1, 'test 3'
    print("TESTS PASSED")
