# imports the os module
import os


# function to display the first (number) of characters
def display_chars(f_path, num_char):

    with open(f_path) as file:
        first_char = file.read(num_char)

    print(f"The first 5 characters are: \n{first_char}")


# function to display the first line
def display_line(f_path):

    with open(f_path) as file:
        first_line = file.readline()

    print(f"\nThe first line is:\n{first_line}")


# function to display all the text in the file
def display_text(f_path):

    with open(f_path) as file:
        file = file.read()

    print(f"The full text is:\n{file}")


# runs the entire program
def run():
    # pre-defines number of characters and file path variables
    f_path = "library.txt"
    num_char = 5

    # calls each function
    display_chars(f_path, num_char)
    display_line(f_path)
    display_text(f_path)


# begins the program
if __name__ == "__main__":
    run()