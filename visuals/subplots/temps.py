# imported modules
import os
import matplotlib.pyplot as plt


# reads the txt file
def read_data(file):
    with open(file) as f:
        temps = [int(x) for x in f.read().split()]

    # returns a list
    return temps


# run function
def run():
    # sets the file path/name
    temps = "temps.txt"
    # gets the temperatures from the file
    y = read_data(temps)
    # days values
    x = [1, 2, 3, 4, 5, 6, 7]

    # plotting two subplots
    fig, (axs1, axs2) = plt.subplots(1, 2)
    # plots line graph
    axs1.plot(x, y)
    axs1.set_ylabel("Temperatures")
    axs1.set_xlabel("Days")
    axs1.set_xlim(1, 7)
    # plots bar graph
    axs2.bar(x, y)
    axs2.set_ylabel("Temperatures")
    axs2.set_xlabel("Days")
    axs2.set_xlim(1, 7)
    # shows the subplots
    plt.show()


# runs the function
run()
