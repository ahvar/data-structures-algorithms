from sortedcontainers import SortedDict


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # TODO: Add the missing method to compare two Player objects based on their score.
    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    # TODO: Also, remember to define how two Player objects are checked for equality.

    def __hash__(self):
        return hash((self.name, self.score))


brad = Player("Brad", 75)
amy = Player("Amy", 87)
tournament = SortedDict()
tournament[75] = brad
tournament[87] = amy
# TODO: Add two Player objects to the tournament. Use name as 'Amy' with score 87 and 'Brad' with score 75. Assign them placements accordingly.

for score, player in tournament.items():
    print(f"Name: {player.name}, Score: {score}")

# Your code here to print the players' details
