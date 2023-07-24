#!/usr/bin/env python3

# Given an integer array of size N. For each element in the array, check whether there exist a smaller element on the next immediate position of the array. If such an element exists, print that element. If there is no smaller element on the immediate next to the element then print -1.

# Output: For each test case, print the next immediate smaller elements for each element in the array.

def return_smaller_eles(s):
    s = s.split(" ")
    s = [int(x) for x in s]
    final = []
    
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            final.append(s[i+1])
        else:
            final.append(-1)

    final.append(-1)
    final = [str(x) for x in final]
    return ' '.join(final)
    
if __name__ == "__main__":
    assert return_smaller_eles("4 2 1 5 3") == "2 1 -1 3 -1", 'error1'
    assert return_smaller_eles("5 6 2 3 1 7") == "-1 2 -1 1 -1 -1", 'error2'
    print("TESTS PASSED")
