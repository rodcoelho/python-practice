#!/usr/bin/env python3

# Given two strings, S and R, composed of only English alphabets (both upper and lower cases), find the alphabets that occur in both the strings. Print the common alphabets (if any) as output in ascending order of their ASCII values.

# Input:
# First line of input is an integer T, denoting the number of test cases. For each test case, first line of input is the string S and second line is the string R. Repetition is allowed in both the strings.

# Output:
# The only line of output for each test case is the list of alphabets that occur in both S and R. Upper and lower case alphabets are treated to be distinct from each other i.e. 'A' and 'a' will be regarded two different letters. The letters are printed on a new line in ascending order of ASCII values i.e. capital letters in common will be printed first in the output. If there are no common letters in S and R, print "nil" as output (without quotes).


def common_chars(s,r):
    payload = []
    s, r = [ord(x) for x in s], [ord(y) for y in r]         # O (N)

    flag = True
    while flag:                                             # O (N)
        flag = False
        for e in s:
            if e in r:
                payload.append(e)
                s.remove(e)
                r.remove(e)
                flag = True

    payload.sort()                                          # O ( Nlog(N) )
    if payload:
        return ''.join([chr(x) for x in payload])           # O ( N )
    else:
        return 'nil'


if __name__ == "__main__":
    assert common_chars('tUvGH', 'Hhev') == 'Hv', 'error1'
    assert common_chars('aabb', 'ccll') == 'nil', 'error2'
    assert common_chars('xYzab', 'YYoxb') == 'Ybx', 'error3'

