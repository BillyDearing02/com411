# gets the user string input
phrase = input("What phrase do you see?\n")
# converts the number of characters into an int variable
number = len(phrase)
# defines reversed variable as a string
reversed = ""
print("\nReversing...\n")
# loops until the end of the phrase
for count in phrase:
    # counts down so you get the reversed phrase
    number = number - 1
    reversed = count + reversed

print(f"The phrase is: {reversed}")