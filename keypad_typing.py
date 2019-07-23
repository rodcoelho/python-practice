#!/usr/bin/env python3

# You are given a string S of alphabet characters and the task is to find its 
# matching decimal representation as on the shown keypad. 
# Output the decimal representation corresponding to the string. For ex: if 
# you are given “amazon” then its corresponding decimal 
# representation will be 262966.

_keypad = {
    'a': 2,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 3,
    'f': 3,
    'g': 4,
    'h': 4,
    'i': 4,
    'j': 5,
    'k': 5,
    'l': 5,
    'm': 6,
    'n': 6,
    'o': 6,
    'p': 7,
    'q': 7,
    'r': 7,
    's': 7,
    't': 8,
    'u': 8,
    'v': 8,
    'w': 9,
    'x': 9,
    'y': 9,
    'z': 9
}

def get_dec(word):
    dec = ''
    for char in word:
        dec += str(_keypad[char])
    return int(dec)


if __name__ == "__main__":
    assert get_dec('geeksforgeeks') == 4335736743357, 'error 1'
    assert get_dec('geeksquiz') == 433577849, 'error 2'
    print("TESTS PASSED")
