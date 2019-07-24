#!/usr/bin/env python3

# Given an array A of positive integers. Your task is to sort
# them in such a way that the first part of the array contains
# odd numbers sorted in descending order, rest portion contains
# even numbers sorted in ascending order.


def custom_sort(nums):
    list_nums = [int(num) for num in nums.split(' ')]
    presort_evens = []
    presort_odds = []
    for num in list_nums:
        if num % 2 == 0:
            presort_evens.append(num)
        else:
            presort_odds.append(num)

    evens = ' '.join([str(num) for num in sorted(presort_evens)])
    odds = ' '.join([str(num) for num in sorted(presort_odds, reverse=True)])
    return odds + ' ' + evens


if __name__ == "__main__":
    assert custom_sort("1 2 3 5 4 7 10") == "7 5 3 1 2 4 10", 'error 1'
    assert custom_sort("0 4 5 3 7 2 1") == "7 5 3 1 0 2 4", 'error 2'
    print("TESTS PASSED")
