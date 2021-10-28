# Input
# Gets the users name
name = input("What is your name Human?")
# Gets the users age
age = input("How old are you (in years)?")
# Gets the users height and allocates it as a float point variable
height = float(input("How tall are you (in meters)?"))
# Gets the users height and allocates it as a integer variable
weight = int(input("How much do you weigh (in kilograms)?"))
# Calculates the users bmi
bmi = str(round(weight / height, 2))
# Output
print(f"{name} you are {age} and your bmi is {bmi}")