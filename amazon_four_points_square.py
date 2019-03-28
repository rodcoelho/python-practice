#!/usr/bin/env python3

# Given coordinates of four points in a plane, find if the four points form a square or not.

# Output: For each test case print 1 if the four points form a square else print 0. Remember to output the answer of each test case in a new line.
 

def check_square(s):
    arr = s.split(' ')
    arr = [int(x) for x in arr]
    
    if len(arr) != 8:
        return 0

    #arr2 = []
    #tmp = []
    #for i in range(len(arr)):
    #    tmp.append(arr[i])
    #    if len(tmp) == 2:
    #        arr2.append(tmp)
    #        tmp = []

    for ele in arr:
        if arr.count(ele) < 3:
            return 0
    return 1    


if __name__ == "__main__":
    assert check_square("20 20 20 10 10 20 10 10") == 1, 'error1'
    assert check_square("10 10 10 10 20 10 20 30") == 0, 'error2'
    assert check_square("1") == 0, 'error3'
    print("TESTS PASSED")
