#!/usr/bin/env python3

# Provided a String of length N, your task is to find out whether or not the given string is a prime string. A prime string is a string in which the sum of the ASCII value of all the characters is prime.


def prime_string(s):
    # make string list and make chars into nums
    s = sum([ord(x) for x in s])

    # check if num is prime
    if s == 2:
        return "YES"
    if s % 2 == 0 or s < 2:
        return "NO"
    for n in range(3, int(s/2), 2):
        if s % n == 0:
            return "NO"
    return "YES"


if __name__ == "__main__":
    assert prime_string('prime') == 'YES', 'error1'
    assert prime_string('geeksforgeeks') == 'YES', 'error2'
    assert prime_string('rodrigo') == 'NO', 'error3'
    assert prime_string('even') == 'NO', 'error4'
    assert prime_string('odd') == 'YES', 'error5'

