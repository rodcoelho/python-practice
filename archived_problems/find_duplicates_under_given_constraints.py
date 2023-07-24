#!/usr/bin/env python3

# Given a sorted array having 10 elements which contains 
# 6 different numbers in which only 1 number is repeated 
# five times. Your task is to find the duplicate number 
# using two comparisons only.


def get_dups(nums):
    if nums[3] == nums[4]:
        return nums[3]
    elif nums[5] == nums[6]:
        return nums[5]
    return -1


if __name__ == "__main__":
    assert get_dups([1, 2, 4, 5, 6, 9, 9, 9, 9, 9]) == 9, 'test 1'
    assert get_dups([1, 2, 3, 3, 3, 3, 3, 5, 9, 10]) == 3, 'test 2'
    assert get_dups([1, 1, 1, 1, 1, 2, 3, 4, 5, 6]) == 1, 'test 3'
    assert get_dups([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1, 'test 4'
    print("TESTS PASSED")


