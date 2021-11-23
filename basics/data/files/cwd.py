# imports the os module
import os


# working directory function output
def cwd():
    # gets the file path
    path = os.getcwd()
    print(f"Current Working Directory: {path}\n")

    # prints what files are in the directory
    print(f"The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run():
    # prints a statement and then calls the first function
    print("Processing...\n")
    cwd()


# begins the program
run()