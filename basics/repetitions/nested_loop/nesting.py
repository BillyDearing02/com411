# User input for Sequence
markerSequence = input("Please enter a sequence\n")
# gets the marker from the user
marker = input("Please enter the character for the marker.\n")
# defines int variables
range = 0
dash = 0
# has a while loop until the code had found 2 markers
while range < 2:
    # uses a membership operator to go through each character in the string
    for check in markerSequence:
        # if/elif statement to check each marker
        if check == marker:
            range = range + 1
        elif range != 2 and range != 0:
            # counter until both markers have been through the for loop
            dash = dash + 1

print(f"\nThe distance between the markers is {dash}.")