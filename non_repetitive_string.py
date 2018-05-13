#!/usr/bin/env python3

# Shreyansh has been given a string for evaluation by his teacher. He needs to find out whether the given string is non-repetitive or not.
# A non-repetitive string is defined as a string which does not contain any different character between 2 same characters (Refer example for explanation).


def find_rep(s):
    payload = 1
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    for key, values in d.items():
        if len(values) > 1:
            if values[-1] - values[0] != len(values) - 1:
                payload = 0
    return payload


if __name__ == "__main__":
    assert find_rep('AAABCDD') == 1, 'error 1'
    assert find_rep('AABBAA') == 0, 'error 2'
    assert find_rep('ABCDA') == 0, 'error 3'

