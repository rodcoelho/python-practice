#!/usr/bin/env python3

# Find and print the uncommon characters of the two given strings S1 and S2. Here uncommon character means that either the character is present in one string or it is present in other string but not in both. The strings contains only lowercase characters and can contain duplicates.

# Output: For each testcase, in a new line, print the uncommon characters of the two given strings in sorted order.


def get_uncommon(s1,s2):
    final = []
    for char in s1:
        if char not in s2:
            final.append(char)
    for char in s2:
        if char not in s1:
            final.append(char)

    final = sorted(list(set(final)))
    return ''.join(final)

if __name__ == "__main__":
    assert get_uncommon('characters','alphabets') == 'bclpr', 'error1'
    print("TESTS PASSED")
