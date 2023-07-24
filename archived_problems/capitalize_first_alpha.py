#!/usr/bin/env python3

# Create a function such that an input, such as '1992rod', will return '1992Rod'


def capitalize(dname):
    payload = ''
    for i in range(len(dname)):
        if dname[i].isalpha():
            payload += dname[:i] + dname[i:].capitalize()
            break
    if len(payload) == 0:
        payload = dname
    return payload


if __name__ == '__main__':
    assert capitalize('09121992rodrigo') == '09121992Rodrigo', 'error1'
    assert capitalize('99') == '99', 'error2'
    assert capitalize('rod99') == 'Rod99', 'error3'
    assert capitalize('9iii0') == '9Iii0', 'error4'
    assert capitalize('rod coelho') == 'Rod coelho', 'error5'

