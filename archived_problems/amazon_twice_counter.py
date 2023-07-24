#!/usr/bin/env python3

# Given an array of n words. Some words are repeated twice, we need count such words.

#Output: Print the count of the words which are repeated twice in the string.


def get_count_of_twice(s):
    count = 0
    words_list = s.split(' ')
    unique_words = set(words_list)
    for word in unique_words:
        if words_list.count(word) == 2:
            count += 1

    print(count)
    return count


if __name__ == '__main__':
    assert get_count_of_twice('hate love peace love peace hate love peace love peace') == 1, 'error1'
    assert get_count_of_twice('Tom Jerry Thomas Tom Jerry Courage Tom Courage') == 2, 'error 2'
    print("ALL TESTS PASSED")
