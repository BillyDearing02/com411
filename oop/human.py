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


if __name__ == "__main__":
    human = Human()
    human.display()