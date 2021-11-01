# Gets the users string input
marking = input("What strange markings do you see?\n")

print("\nIdentifying...\n")
counter = 0
# for loop up to a range of 0 - number of characters
for count in range(0, len(marking)):
    # indexs the marking string variable
    print(f"index {counter}: {marking[counter]}")
    counter = counter + 1

print("Done!")
