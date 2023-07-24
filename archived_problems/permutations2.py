#!/usr/bin/env python3

import itertools

finalproduct = []
word = 'abcd'

for x in range(1, len(word)+1):
    finalproduct += [''.join(i) for i in itertools.permutations(word, x)]

print(sorted(set(finalproduct)))

