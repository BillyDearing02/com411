# function that required two parameters to run
def climb_ladder(step_remaining, step_crossed):
    # if statement to check if the steps remaining is greater than the steps that have been crossed
    if step_remaining > step_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


# calls the function to test both the if and the else statement
climb_ladder(5, 2)
climb_ladder(2, 5)