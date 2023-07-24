#!/usr/bin/env python3

# Write a function that transforms a string into title case. This mostly means capitalizing only every first letter of every word in the string. However, there are some non-obvious exceptions to title case which can't easily be hard-coded. Your function must accept, as a second argument, a set or list of words that should not be capitalized.
# Furthermore, the first word of every title should always have a capital leter.

# Test Case:
# >>> exceptions = ['jumps', 'the', 'over']
# >>> titlecase('the quick brown fox jumps over the lazy dog', exceptions)
# "The Quick Brown Fox jumps over the Lazy Dog"
#
# >>> exceptions = ['are', 'is', 'in', 'your', 'my']
# >>> titlecase('THE vitamins ARE IN my fresh CALIFORNIA raisins', exceptions)
# "The Vitamins are in my Fresh California Raisins"


def title_case(phrase, exceptions):
    phrase_list = [x.lower() for x in phrase.split(' ')]

    for i in range(len(phrase_list)):
        if phrase_list[i] not in exceptions:
            phrase_list[i] = phrase_list[i].capitalize()
        phrase_list[0] = phrase_list[0].capitalize()

    print(' '.join(phrase_list))


if __name__ == '__main__':
    title_case('THE vitamins ARE IN my fresh CALIFORNIA raisins', ['the', 'over'])

