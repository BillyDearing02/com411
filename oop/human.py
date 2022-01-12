class Human:
    # A class attribute (A constant)
    MAX_ENERGY = 100

    # An initialiser (special instance method)
    def __init__(self, name="Human", age=0):
        # instance attributes
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    # An instance method
    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1

    def __repr__(self):
        return f'human(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old.'


if __name__ == "__main__":
    human = Human()
    human.display()
    print(repr(human))
    print(human)
    human.grow()
    human.display()
    print(repr(human))
    print(human)