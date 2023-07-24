#!/usr/bin/env python3

import collections

Card = collections.namedtuple('Card', ['number', 'color'])


class Deck:
    ranks = [str(x) for x in range(0, 9)] + ['skip', 'draw2', 'reverse']
    color = 'blue red yellow green'.split()
    special = ['wild', 'draw4']

    def __init__(self):
        self._cards = [Card(ranks, color) for color in self.color for ranks in self.ranks] + [Card(special, 'black') for special in self.special] * 4

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    deck = Deck()
    print(len(deck))
    for i in range(len(deck)):
        print(deck[i])

