"""
Use of a 2D Array in TicTacToe
 - New game instance represents an empty board
 - mark(i,j) adds a mark at the given position for the current player
"""

from rich import print as rprint
from abc import ABC, abstractmethod


class Player(ABC):
    """"""

    def __init__(self):
        self._moves = []

    @abstractmethod
    def make_move(self, i, j):
        pass


class X(Player):
    """"""

    def __init__(self):
        super().__init__()

    def make_move(self):
        """"""


class O(Player):
    """"""

    def __init__(self):
        super().__init__()

    def make_move(self):
        """"""


class TicTacToe:
    def __init__(self, x, o):
        self._board = [[" "] * 3 for i in range(3)]
        self._x = X()
        self._o = O()

    def mark(i, j):
        pass

    @property
    def board(self):
        return self._board


if __name__ == "__main__":
    x = X()
    o = O()
    ttt = TicTacToe(x, o)
