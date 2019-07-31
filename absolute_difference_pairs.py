#!/usr/bin/env python3

# absolute difference
# Given a list of integers nums, find the number of unique 
# pairs that have abs diff of k

# def Pairs(nums, k) -> int (count of number of unique pairs)
# [1, 2, 3, 4, 5], k = 1 => 4
# [1, 3, 1, 5, 4, 1], k = 0 => 1 

from itertools import combinations


def Pairs(nums, k):
    semi_final_pairs = []
    
    all_combs = combinations(nums, 2)
    
    for combs in list(all_combs):
        if abs(combs[1] - combs[0]) == abs(k):
            semi_final_pairs.append(combs)
            
    final_pairs = set(semi_final_pairs)

    return len(final_pairs)


if __name__ == "__main__":
    assert Pairs([1, 2, 3, 4, 5], 1) == 4, 'test 1'
    assert Pairs([1, 3, 1, 5, 4, 1], 0) == 1, 'test 2'
    assert Pairs([-1, 2, 3, 4, 5], 1) == 3, 'test 3'
    print("TESTS PASSED")

