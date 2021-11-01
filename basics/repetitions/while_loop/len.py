# len input for amount
amount = len(input("Please enter a phrase:\n"))
output = ""
while amount > 0:
    # decreases amount by 1 until it equals zero
    amount = amount - 1
    # add the string bop to the output string variable
    output = output + "Bop "

print(output)