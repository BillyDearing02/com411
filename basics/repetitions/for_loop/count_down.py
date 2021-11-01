# amount input set as an int
amount = int(input("How far are we from the cave?\n"))

# use of for to output the amount the user inputted
for count in range (0, amount):
    print(f"{amount} steps remaining")
    # counter to decrease the amount for each loop
    amount = amount - 1

print("\nWe have reached the cave!")