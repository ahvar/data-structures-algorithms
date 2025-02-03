from sortedcontainers import SortedDict


from sortedcontainers import SortedDict


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.score))


people = SortedDict()

john = Person("John", 30)
alice = Person("Alice", 25)

people[john] = "Programmer"
people[alice] = "Designer"
