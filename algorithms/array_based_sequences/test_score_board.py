import unittest

from algorithms.array_based_sequences.score_board import GameEntry, ScoreBoard


class TestScoreBoard(unittest.TestCase):

    def setUp(self):
        self.jeb = GameEntry("Jebediah", 5)
        self.tuna = GameEntry("Tuna", 10)
        self.arnold = GameEntry("Arnold", 15)
        self.score_board = ScoreBoard(10)

    def test_add(self):
        self.score_board.add(self.jeb)
        self.score_board.add(self.tuna)
        self.score_board.add(self.arnold)
        print(self.score_board.board[0])
        assert self.score_board.board[0] == self.arnold
        assert self.score_board.board[1] == self.tuna
        assert self.score_board.board[2] == self.jeb
