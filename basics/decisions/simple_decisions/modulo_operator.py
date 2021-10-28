# Gets user input for number
number = int(input("Please enter a whole number.\n"))
# Checks whether or not the number is even
if number % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"
# prints output based on user input
print(f"The number {number} is an {parity} number.")