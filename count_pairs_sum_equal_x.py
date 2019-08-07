#!/usr/bin/env python3

# Given two linked list of size N1 and N2 respectively of
# distinct elements, your task is to complete the function 
# countPairs(), which returns the count of all pairs from 
# both lists whose sum is equal to the given value X. 


def countPairs(n1, n2, x):
    n1 = [int(num) for num in n1.split(' ')]
    n2 = [int(num) for num in n2.split(' ')]
    count = 0
    for i in range(len(n1)):
        for j in range(len(n2)):
            if n1[i] + n2[j] == x:
                count += 1
    return count


if __name__ == "__main__":
    assert countPairs("1 2 3 4 5 6", "11 12 13", 15) == 3, 'test 1'
    assert countPairs("7 5 1 3", "3 5 2 8", 10) == 2, 'test 2'
    print("TESTS PASSED")
