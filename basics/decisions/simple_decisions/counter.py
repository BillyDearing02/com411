# inputs to get each number
fNumber = int(input("Please enter the first number\n"))

sNumber = int(input("Please enter the second number\n"))

tNumber = int(input("Please enter the third number\n"))

# puts the 3 numbers into an array to be used in the foreach loop
numberList = [fNumber, sNumber, tNumber]
# defines the 2 variables needs for the loop
even = 0
odd = 0

# goes through each variable in the numberList array
for number in numberList:
    # uses a basic if and else statement to add up the amount of odd and even numbers
    if number % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

# prints how many odd and even numbers the user has inputted
print(f"\nThere were {even} even and {odd} odd.")