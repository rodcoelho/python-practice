#!/usr/bin/env python3

import enchant

from itertools import permutations

english_dictionary = enchant.Dict('en_US')

sticker = 'awspopuploft'

perms = (''.join(x) for x in (permutations(sticker, len(sticker))) if english_dictionary.check(''.join(x)))

for _ in perms:
    print(_)