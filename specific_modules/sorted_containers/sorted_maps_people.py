from sortedcontainers import SortedDict


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return (self.age, self.name) < (other.age, other.name)

    def __gt__(self, other):
        return (self.age, self.name) > (other.age, other.name)

    def __eq__(self, other):
        return (self.age, self.name) == (other.age, other.name)

    def __ne__(self, other):
        return (self.age, self.name) != (other.age, other.name)

    def __hash__(self):
        return hash((self.name, self.age))


people = SortedDict()

john = Person("John", 30)
alice = Person("Alice", 25)

people[john] = "Programmer"
people[alice] = "Designer"

for person in people:
    print(f"{person.name} is a {people[person]}")
# Output:
# Alice is a Designer
# John is a Programmer
