# defining each variable as an int
amount = 0
ans = 0
# loops until 100
while amount < 100:
    # adds 1 until it hits 100
    amount = amount + 1
    # add amount to the current total while looping
    ans = ans + amount
# prints the sum of the first 100 numbers
print("Calculating the sum of the first 100 numbers....\n"
      f"...Done! The answer is {ans}.")