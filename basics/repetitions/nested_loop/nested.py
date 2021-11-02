# defines rows as an int variable and gets how many rows the user wants
rows = int(input("How many rows should I have?\n"))
# defines columns as an int variable and gets how many columns the user wants
columns = int(input("How many columns should I have?\n"))

print("\nHere I go:\n")

# initial for loop is for outputting the amount of user inputted rows
for count in range(0, rows):
    # nested for loop is for outputting the amount of user inputted columns
    for number in range(0, columns):
        print(f":-)", end="")
    # this is for displaying a new line
    print()