#!/usr/bin/env python3

# Your task is to implement the function strstr. 
# The function takes two strings as arguments (s,x) and 
# locates the occurrence of the string x in the string s. 
# The function returns and integer denoting the first
# occurrence of the string x in s.


def strstr(big, small):
    if small not in big:
        return -1
    return big.find(small)


if __name__ == "__main__":
    assert strstr('GeeksForGeeks', 'Fr') == -1, 'error 1'
    assert strstr('GeeksForGeeks', 'For') == 5, 'error 2'
    print("TESTS PASSED")
