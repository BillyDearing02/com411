# imports plotting graphs package
import matplotlib.pyplot as plt

# input coordinate function
def coordinate():
    x = int(input("Please enter a x value"))
    y = int(input("Please enter a y value"))

    return x,y


# path function
def path():
    # prints Retrieving path
    print("Retrieving path...")
    # defines the values as lists
    x_values = []
    y_values = []
    # defines count as an int
    count = 0
    # loops until count = 4
    while count != 4:
        # defines x and y as int
        x = 0
        y = 0
        # counter for the while loop
        count = count + 1
        # gets x and y from coordinate function
        x, y = coordinate()
        # adds them to the list
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


def run():
    # gets the x and y value lists
    x, y = path()
    # plots the graph
    plt.plot(x, y, "ro--")
    # shows the graph
    plt.show()

# calls the initial function
run()