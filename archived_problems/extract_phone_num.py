#!/usr/bin/env python3

# extract the phone number from the string
# The phone number is of the format +dd-ddddddddddd.


def extract_phone_num(s):
    for i in range(len(s)):
        if s[i] == '+':
            if s[i + 3] == '-':
                return s[i:i+15]


if __name__ == '__main__':
    assert extract_phone_num('Call me +91-90549385612.') == '+91-90549385612', 'error1'
    assert extract_phone_num('The number is +24-01087860699') == '+24-01087860699', 'error2'


