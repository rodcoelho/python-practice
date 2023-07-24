#!/usr/bin/env python3

# Given two strings s1 and s2, remove those characters from first string which are present in second string.

def remove_char(s1, s2):
    final = list(s1)
    s2list = list(s2)
    for c in s2list:
        final = [x for x in final if x != c]
    return ''.join(final)

if __name__ == "__main__":
    assert remove_char("geeksforgeeks", "mask") == "geeforgee", 'error1'
    assert remove_char("removeccharaterfrom", "string") == "emovecchaaefom", 'error2'
    print("TESTS PASSED")
