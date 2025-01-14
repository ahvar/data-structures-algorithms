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
        return "({0}, {1})".format(self._name, self._score)


class ScoreBoard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def _resize(self, capacity):
        pass

    def add(self, entry):
        """Consider adding entry to high scores"""
        if not self._board:
            self._board.append(entry)
        elif self._n == len(self._board - 1):
            self._resize(self._n * 2)
        else:
            i = self._n // 2
            if self._board[i].score < entry.score:
                while i > 0 and self._board[i].score != entry.score:
                    i -= 1
            elif self._board[i].score > entry.score:
                while i < self._n - 1 and self._board[i].score != entry.score:
                    i += 1
            if i == self._n - 1 and entry.score < self._board[i].score:
                self._board[i] = entry
            else:
                # move all scores to the right
                j = self._n - 1
                while j > i:
                    self._board[j] = self._board[j + 1]
                    j -= 1
                self._board[j] = entry
