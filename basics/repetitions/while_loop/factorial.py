# sets the input as an int/getting user input
number = int(input("Please enter a number.\n"))
# ans has equal 1 not 0 to be multiplied / defining as int variables
ans = 1
factorial = 0
# loops until number
while number > 0:
    number = number - 1
    factorial = factorial + 1
    ans = ans * factorial

print(f"\nThe factorial is {ans}.")