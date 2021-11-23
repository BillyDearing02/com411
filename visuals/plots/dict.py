# imports plotting graphs package
import random as rand
import matplotlib.pyplot as plt


def data():
    paths = {}
    line = input("What type of line would you like?")
    colour = input("What type of colour would you like?")
    marker = input("What type of marker would you like?")
    paths.update({'linestyle': line, 'colourist': colour, 'markerstyle': marker})

    return paths


def generate():
    lines = int(input("How many lines would you like to display?"))
    for count in range(0, lines):
        x = rand.random()
        y = rand.random()

        values = data()
        print(values)
        print(x)
        print(y)
        plt.plot(x, y, values)


def run():
    print("Running....")
    generate()
    plt.show()
    print("Done!")


generate()
