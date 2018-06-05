#!/usr/bin/env python3

# Given a str that contains special chars, reverse all regular chars but leave special chars in exact location


def reverse_str_leave_special(s):
    s = list(s)
    temp = []
    chars = []
    final = []

    # separate characters
    for _ in s:
        if _.isalpha():
            chars.append(_)
            temp.append("_")
        else:
            temp.append(_)

    # reverse the characters
    chars = chars[::-1]

    # add back characters
    for _ in temp:
        if _ == '_':
            final.append(chars[0])
            chars = chars[1:]
        else:
            final.append(_)

    return "".join(final)


if __name__ == '__main__':
    assert reverse_str_leave_special("a,b$c") == "c,b$a", 'error1'
    assert reverse_str_leave_special("Ab,c,de!$") == "ed,c,bA!$", 'error2'

