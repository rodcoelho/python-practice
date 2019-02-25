#!/usr/bin/env python3

# Given an array A (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output i.e you have to iterate on the original array only.

# Output: For each testcase, print the array in Zig-Zag fashion.


def convert_zig(arr):
    arr = arr.split(" ")
    less = True
    final = arr[:]
    for i in range(len(arr) - 1):
        if less:
            if final[i] > final[i+1]:
                final[i], final[i+1] = final[i+1], final[i]    
            less = False
        else:
            if final[i] < final[i+1]:
                final[i], final[i+1] = final[i+1], final[i]
            less = True
    #print(final)
    return ' '.join(final)
        

if __name__ == "__main__":
    assert convert_zig("4 3 7 8 6 2 1") == "3 7 4 8 2 6 1", 'error1'
    assert convert_zig("1 4 3 2") == "1 4 2 3", 'error2'
    print("TESTS PASSED")

