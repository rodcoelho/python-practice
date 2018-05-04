#!/usr/bin/env python3

# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
#
#
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2


def last2(str):
    l2 = str[-2:]
    s = str[:-2]
    count = 0
    for i in range(len(s)):
        try:
            if s[i] == l2[0]:
                if s[i+1] == l2[1]:
                    count += 1
        except:
            pass
    return count

