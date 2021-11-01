number = int(input("Please enter a number.\n"))
ans = 1
factorial = 0
while number > 0:
    number = number - 1
    factorial = factorial + 1
    ans = ans * factorial

print(f"\nThe factorial is {ans}.")