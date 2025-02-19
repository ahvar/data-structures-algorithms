import unittest

from score_board import GameEntry, ScoreBoard


class TestScoreBoard(unittest.TestCase):

    def setUp(self):
        self.arthur = GameEntry("Arthur", 22)
        self.carlo = GameEntry("Carlo", 44)
        self.anna = GameEntry("Anna", 33)
        self.score_board = ScoreBoard(10)

    def test_add(self):
        self.score_board.add(self.arthur)
        self.score_board.add(self.carlo)
        self.score_board.add(self.anna)
