#!/usr/bin/env python3

# Given strings s1 and s2, you need to find if s2 is a 
# rotated version of the string s1. The strings are lowercase.


def check_rotation(s1, s2):
    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2:
            return 1
    return 0


if __name__ == "__main__":
    assert check_rotation('geeksforgeeks', 'forgeeksgeeks') == 1, 'test 1'
    assert check_rotation('mightandmagic', 'andmagicmigth') == 0, 'test 2'
    assert check_rotation('mushroomkingdom', 'itsamemario') == 0, 'test 3'
    assert check_rotation('geekofgeeks', 'geeksgeekof') == 1, 'test 4'
    print("TESTS PASSED")
