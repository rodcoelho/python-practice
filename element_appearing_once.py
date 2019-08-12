#!/usr/bin/env python3

# Given an sorted array A[i] of N positive integers having
# all the numbers occuring exactly twice, except for one
# number which will occur only once. Find the number occuring 
# only once.


def get_single(nums):
    nums = [int(num) for num in nums.split(' ')]
    ret_val = nums[-1]

    for i in range(0, len(nums), 2):
        if i == len(nums) - 1:
            break

        if nums[i] != nums[i + 1]:
            ret_val = nums[i]
            break

    return ret_val


if __name__ == "__main__":
    assert get_single('1 1 2 5 5') == 2, 'test 1'
    assert get_single('2 2 5 5 20 30 30') == 20, 'test 2'
    assert get_single('1 1 2') == 2, 'test 3'
    assert get_single('1 2 2') == 1, 'test 4'
    print("TESTS PASSED")
