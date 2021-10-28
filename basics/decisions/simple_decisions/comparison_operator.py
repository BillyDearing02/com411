# Gets first number from user
fNumber = int(input("Please enter the first number.\n"))
# Gets second number from user
sNumber = int(input("Please enter the second number.\n"))

# checks which condition the user input meets and outputs the appropriate response.
if fNumber > sNumber:
    print("\nThe second number is the smallest!")
elif fNumber < sNumber:
    print("The first number is the smallest!")
else:
    print("They're both equal!")




