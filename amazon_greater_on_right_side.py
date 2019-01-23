#!/usr/bin/env python3

# You are given an array A of size N. Replace every element with the next greatest element (greatest element on its right side) in the array. Also, since there is no element next to the last element, replace it with -1.

# Input:
# The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line is N, the size of tha array. The second line contains N space separated integers.

# Output:
# For each testcase, print the modified array.


def get_greater(l):
    output = []
    for i in range(1, len(l)):
        tmp = l[i:]
        output.append(max(tmp))
    output.append(-1)
    print(output)
    return output
        


if __name__ == '__main__':
    print("beginning tests...")
    assert get_greater([16, 17, 4, 3, 5, 2]) == [17, 5, 5, 5, 2, -1], 'error1'
    assert get_greater([2, 3, 1, 9]) == [9, 9, 9, -1], 'error2'
    print("TESTS PASSED!")
