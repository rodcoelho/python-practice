#!/usr/bin/env python3

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    deck = Deck()
    favorite_card = deck._cards[-1]

    assert len(deck) == 52, 'len error'
    assert favorite_card == Card(rank='A', suit='hearts'), 'card error'
    assert deck[51] == favorite_card, 'error3'

