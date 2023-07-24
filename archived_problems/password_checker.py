#!/usr/bin/env python3

# at least 8 len
# one uppercase
# one special character


def check_password(s):
    special = ['#','@','%']
    if len(s) < 8:
        return False
    if s.lower() == s:
        return False
    if any(char in special for char in s):
        return True
    else:
        return False


if __name__ == '__main__':
    assert check_password("animals#@") == False, "error1"
    assert check_password("Animals#@") == True, "error2"
    assert check_password("Als#@") == False, "error3"
    assert check_password("Rodrigo") == False, "error4"

