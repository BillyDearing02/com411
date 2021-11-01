# sets the input as an int/ getting user input
amount = int(input("How many number should I sum up?\n"))
# setting counter to equal amount
counter = amount
# defining each variable as an int
number = 0
ans = 0
# loops until counter is not greater than 0
while counter > 0:
    # makes the counter count down by increments of 1
    counter = counter - 1
    # adds 1 each loop for the input
    number = number + 1
    # uses the number counter and the pre-defined amount of numbers to sum up
    uNumber = int(input(f"Please enter number {number} of {amount}\n"))
    # sums up all of the numbers the user has inputted
    ans = ans + uNumber
# outputs the sum
print(f"\nThe answer is {ans}.")