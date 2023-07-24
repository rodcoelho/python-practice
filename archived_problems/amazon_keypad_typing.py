#!/usr/bin/env python3

# You are given a string S of alphabet characters and the task is to find its matching decimal representation as on the shown keypad. Output the decimal representation corresponding to the string. For ex: if you are given “amazon” then its corresponding decimal representation will be 262966.

# Output: For each test case, print in a new line, the corresponding decimal representation of the given string.


dial_pad = [[],['a','b','c'],['d','e','f'],['g','h','i'], ['j','k','l'],['m','n','o'],['p','q','r','s'], ['t','u','v'],['w','x','y','z'] ]

dial_dict = {}

for i in range(len(dial_pad)):
    for letter in dial_pad[i]:
        dial_dict[letter] = str(i+1)


def get_dialpad(s):
    decimal = ''
    for char in s:
        try:
            decimal += dial_dict[char.lower()]
        except:
            pass
    decimal = int(decimal)

    return decimal


if __name__ == '__main__':
    assert get_dialpad('geeksforgeeks') == 4335736743357, 'error1'
    assert get_dialpad('geeksquiz') == 433577849, 'error2'
    print("TESTS PASSED")
