#!/usr/bin/env python3


# sort string in reverse

# EASY
def sort_string_in_rev(s):
    return s[::-1]

# MEDIUM
def custom_bub_sort(s):
    s = list(s)
    ssorted = False

    while not ssorted:
        ssorted = True
        for i in range(len(s)-1):
            if s[i] < s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
                ssorted = False
    return (''.join(s))


if __name__ == "__main__":
    assert custom_bub_sort('aaabanimal') == 'nmlibaaaaa', 'error 1'

