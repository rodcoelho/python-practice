
"""
The Game of Master is played as below:

The computer has four slots containing balls that are red(R), yellow(Y), green(G), or blue(B).

For example:
    the computer might have RGGB
    (e.g.,Slot#1 is red,Slot#2 and Slot#3 are green,Slot#4 is blue).

You, the user, are trying to guess the solution. You might,for example,guess YRGB.

When you guess the correct color for the correct slot,you get a "hit".
If you guess a color that exists but is in the wrong slot,you get a "pseudo-hit".
For example:the guess YGRB has 2 hits and 1 pseudo hit.
 
For each guess,you are told the number of hits and pseudo-hits.
Write a method that,given a guess and a solution,
returns the number of hits and pseudo hits.
"""

import unittest

class GameOfMaster:
    NEUTRAL_SYMBOL = "x"
    def __init__(self, slots):
        self.slots = self._normalize_colors(slots)

    def _normalize_colors(self, colors):
        return [char for char in colors]

    def _neutralize_slot(self, slot, index):
        slot[index] = self.NEUTRAL_SYMBOL
        print(slot)
    
    def handle_guess(self, colors):
        hits = 0
        pseudo_hits = 0
        non_match_guess = []
        non_match_slots = []
        colors = self._normalize_colors(colors)
        for i in range(len(self.slots)):
            if self.slots[i] == colors[i]:
                hits += 1
                self._neutralize_slot(self.slots, i)
                self._neutralize_slot(colors, i)
            else:
                non_match_slots.append(self.slots[i])
                non_match_guess.append(colors[i])

        print("non_match_guess", non_match_guess)
        print("non_match_slots", non_match_slots)
        
        i = 0
        while i < len(non_match_guess):
            if non_match_guess[i] in non_match_slots:
                element = non_match_guess.pop(i)
                non_match_slots.remove(element)
                pseudo_hits += 1

            else:
                i += 1

        return hits, pseudo_hits
                    
class TestGameOfMaster(unittest.TestCase):
    def test_handle_guess(self):

        gom = GameOfMaster("RYGB")
        self.assertEqual(gom.handle_guess("RYGB"), (4, 0))
        
        gom = GameOfMaster("RYGB")
        self.assertEqual(gom.handle_guess("RYGR"), (3, 0))

        gom = GameOfMaster("RYGB")
        self.assertEqual(gom.handle_guess("RYBG"), (2, 2))

        gom = GameOfMaster("RYGB")
        self.assertEqual(gom.handle_guess("RRRB"), (2, 0))

        gom = GameOfMaster("RRGB")
        self.assertEqual(gom.handle_guess("RRRB"), (3, 0))

        gom = GameOfMaster("RYGB")
        self.assertEqual(gom.handle_guess("GBRY"), (0, 4))

unittest.main()