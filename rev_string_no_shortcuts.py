#!/usr/bin/env python3

# reverse a string without using pythonic shortcuts


def rev_str(s):
    payload = []
    s = list(s)
    for i in range(len(s)):
        payload = [s[i]] + payload
    return ''.join(payload)


if __name__ == '__main__':
    assert rev_str('animals') == 'slamina', 'error1'
    assert rev_str('rodrigo') == 'ogirdor', 'error2'
    assert rev_str('abc') == 'cba', 'error3'
    assert rev_str('aaa') == 'aaa', 'error4'