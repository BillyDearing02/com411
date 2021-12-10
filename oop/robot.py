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


if __name__ == "__main__":
    robot = Robot()
    robot.display()
