# int input for amount
amount = int(input("How many bars should be charged?\n"))
charge = 0
# checks if amount is great than zero
while amount > 0:
    # decreases amount by 1 until it equals zero
    amount = amount - 1
    # increases charge by 1 until amount equals zero
    charge = charge + 1
    # multiples the bar by charge
    bars = "█ " * charge
    print(f"Charging: {bars}")

print("\nThe battery is fully charged.")