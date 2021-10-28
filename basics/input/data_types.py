# Input
# Gets the users name
name = input("What is your name Human?")
# Gets the users age
age = int(input("How old are you (in years)?"))
# Gets the users height and allocates it as a float point variable
height = float(input("How tall are you (in meters)?"))
# Gets the users weight and allocates it as a integer variable
weight = float(input("How much do you weigh (in kilograms)?"))
# Calculates the users bmi
heightSq = float(pow(height, 2))
bmi = float(round(weight / heightSq, 2))
# Output
print(f"{name} you are {age} and your bmi is {bmi}")