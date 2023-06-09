# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/01_deck.ipynb 2
from .card import *
from fastcore.utils import *

# %% ../nbs/01_deck.ipynb 4
class Deck:
    """
        A class representing a deck of cards
    """
    def __init__(self):
        self.cards = [Card(s,r) for s in range(4) for r in range(1,14)]
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return "; \n".join(map(str, self.cards))
    def __contains__(self, card):
        return card in self.cards
    __repr__ = __str__

# %% ../nbs/01_deck.ipynb 15
@patch
def pop(self:Deck,
        idx: int=-1      # The index of the card to remove from the deck, by default it pops the last one
       ):
    """
        Remove the card from the deck
    """
    return self.cards.pop(idx)
