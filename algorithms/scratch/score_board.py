class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def __str__(self):
        return "{}: {}".format(self._name, self._score)


class ScoreBoard:
    def __init__(self, capacity):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, i):
        if not 0 <= i < self._n:
            raise IndexError("Invalid index")
        return self._board[i]

    def add(self, entry):
        if self._n == 0:
            self._board[self._n] = entry
            self._n += 1
        elif self._n > 0:
            j = 0
            while j < self._n and self._board[j].score >= entry.score:
                j += 1
            if j == self._n:
                self._board[j] = entry
            else:
                for k in range(
                    self._n, j, -1
                ):  # shift to the right; start immediately after the last score
                    self._board[k] = self._board[k - 1]
                self._board[k] = entry
                self._n += 1

    def __str__(self):
        return "".join([f"{entry}\n" for entry in self._board])


if __name__ == "__main__":
    arthur = GameEntry("Arthur", 22)
    carlo = GameEntry("Carlo", 44)
    anna = GameEntry("Anna", 33)
    score_board = ScoreBoard(10)
    score_board.add(arthur)
    score_board.add(carlo)
    score_board.add(anna)
    print(score_board)
