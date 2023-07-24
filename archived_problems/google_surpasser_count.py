#!/usr/bin/env python3

# A surpasser of an element of an array is a greater element to its right, therefore x[j] is a surpasser of x[i] if i < j and x[i] < x[j]. The surpasser count of an element is the number of surpassers.
# Given an array of distinct integers, for each element of the array find its surpasser count i.e. count the number of elements to the right that are greater than that element.
 
# Output:  count the number of elements to the right that are greater than that element.

def get_surpasser_array(arr):
    surps = []
    for i in range(len(arr)):
        cnt = 0
        tmp_arr = arr[i:]
        for y in range(len(tmp_arr)):
            if tmp_arr[y] > arr[i]:
                cnt += 1
        surps.append(cnt)
    return surps


if __name__ == '__main__':
    assert get_surpasser_array([4,5,1,2,3]) == [1,0,2,1,0], 'error1'
    print("TESTS PASSED")
