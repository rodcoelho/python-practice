#!/usr/bin/env python3


def rev_sort(s):
    s = list(s)
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(0,len(s)-1):
            if s[i] < s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
                unsorted = True
    return ''.join(s)


if __name__ == '__main__':
    assert rev_sort('abc') == 'cba', 'error1'

