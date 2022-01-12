class Robot:
    # A class attribute (A constant)
    MAX_ENERGY = 100

    # An initialiser (special instance method)
    def __init__(self, name="Robot", age=0, energy=0):
        # instance attributes
        self.name = name
        self.age = age
        self.energy = energy

    # An instance method
    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'

    def grow(self):
        self.age += 1


if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(repr(robot))
    print(robot)
    robot.grow()
    robot.display()
    print(repr(robot))
    print(robot)
