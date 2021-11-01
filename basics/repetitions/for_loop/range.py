# amount input set as an int

amount = int(input("What level of brightness is required?\n"))

print("\nAdjusting brightness...\n")
# defining an int variable
number = 0
# Checking if the user input is even
if amount % 2 == 0:
    for count in range(0, amount, 2):#
        # increments by 2 as its even
        number = number + 2
        # converts the counter number to an *
        ans = "*" * number
        print(f"Beep's brightness level: {ans}")
        print(f"Beep's brightness level: {ans}\n\n")
# in case the user input is odd it increments by 1 instead of 2
else:
    for count in range(0, amount):
        # increments by 1 as its odd.
        number = number + 1
        # converts the counter number to an *
        ans = "*" * number
        print(f"Beep's brightness level: {ans}")
        print(f"Beep's brightness level: {ans}\n\n")

# if you wanted to make both odd and even increment by 2 you could just define the number variable in the if/else statements. For the even number = 0 and for odd number = 1