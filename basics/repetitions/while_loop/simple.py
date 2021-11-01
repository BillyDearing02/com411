# int input for amount
amount = int(input("How many cables should I remove?\n"))
# checks if amount is great than zero
while amount > 0:
    # decreases amount by 1 until it equals zero
    amount = amount - 1
    print("Removed cable.")

