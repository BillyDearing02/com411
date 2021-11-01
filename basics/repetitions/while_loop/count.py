# int input for amount
amount = int(input("How many cables should I remove?\n"))
avoid = 0
# checks if amount is great than zero
while amount > 0:
    # decreases amount by 1 until it equals zero
    amount = amount - 1
    avoid = avoid + 1
    print(f"Avoiding...Done! {avoid} live cables avoided.")