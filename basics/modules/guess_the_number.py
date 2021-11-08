# imports random module and sets it to rnd
import random as rnd


# function to run the program
def play_guess_the_number():
    # defines min and max as integers and prompts the user to enter values for them.
    min = int(input("Please enter the minimum value:\n"))
    max = int(input("Please enter the maximum value:\n"))

    # gets a random number between the min and max with increments of 1
    random_number = rnd.randrange(min, max, 1)

    # defines the users guess as an integer
    user_guess = 0
    # loops until the user guesses correctly
    while user_guess != random_number:
        # gets the users guess
        user_guess = int(input(f"I am thinking of a number between {min} and {max}. Can you guess what it is?"))
        # use of if/elif and else statement to check if is lower/higher or equal to random number
        if user_guess > random_number:
            print("Your guess is too high.")
            print("Try again:")
        elif user_guess < random_number:
            print("Your guess it too low.")
            print("Try again:")
        else:
            print(f"You guessed it! The number im thinking of is {random_number}")


# runs the program
play_guess_the_number()
