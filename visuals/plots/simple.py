# imports plotting graphs package
import matplotlib.pyplot as plt


# defines display as a function that requires 2 parameters
def display(x, y):
    plt.plot(x, y)
    plt.show()


# initial run function to begin the program
def run():
    # sets the x and y values for the graph
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    # calls the display function
    display(x, y)


# calls the initial run function
run()