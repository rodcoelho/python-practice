#!/usr/bin/env python3

# You have been given an alphanumeric string S, extract maximum numeric value from that string. Alphabets will only be in lower case.

# Output: For each testcase, in a new line, print the Maximum number extracted from the string S.


def extract_maximum(s):
    s = [x if x.isdigit() else ' ' for x in s]
    s = ''.join(s).split()
    s = [int(x) for x in s]

    max = 0
    for ele in s:
        if ele > max:
            max = ele

    return max
    


if __name__ == "__main__":
    assert extract_maximum("100klh564abc365bg") == 564, 'error1'
    assert extract_maximum("abvhd9sdnkjdfs") == 9, 'error2'
    assert extract_maximum("abchsd0sdhs") == 0, 'error3'
    assert extract_maximum("abc") == 0, 'error4'
    print("TESTS PASSED")
