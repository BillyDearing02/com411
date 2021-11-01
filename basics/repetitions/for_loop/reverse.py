# gets the user string input
phrase = input("What phrase do you see?\n")
# converts the number of characters into an int variable
number = len(phrase)
# defines reversed variable as a string
reversed = ""
print("\nReversing...\n")
# loops until the end of the phrase
for count in range(0, number):
    # counts down so you get the reversed phrase
    number = number - 1
    reversed = reversed + phrase[number]

print(f"The phrase is: {reversed}")
