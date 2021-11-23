# imports plotting graphs package
import matplotlib.pyplot as plt

# plots the small red square
def small():
    x = [3,3,4,4,3]
    y = [3,4,4,3,3]
    small_plot = plt.plot(x,y, 'ro--')
    return small_plot


# plots the medium green square
def medium():
    x = [2,5,5,2,2]
    y = [2,2,5,5,2]
    medium_plot = plt.plot(x,y, 'gs--')
    return medium_plot


# plots the large blue square
def large():
    x = [1,6,6,1,1]
    y = [1,1,6,6,1]
    large_plot = plt.plot(x,y, 'bx-')
    return large_plot


# runs the function
def run()
    # calls each function
    small()
    medium()
    large()
    # shows the plotted graphs
    plt.show()

run()