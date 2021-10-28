# Gets user input on what the activity is
activity = input("Please enter the activity to be performed.\n")

# checks if the activity is calculate
if activity == "calculate":
    # makes the perform variable equal calculations
    perform = "Calculations"
else:
    # makes the perform variable equal activity if the if statement condition isnt met
    perform = "Activity"

# prints output based on the if statement
print(f"Performing {perform}...\n\n"
      "Activity completed!")