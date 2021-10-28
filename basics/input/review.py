# Input
# Gets the users name
name = input("What is your name Human?\n")
# Gets the users age
age = int(input("How old are you (in years)?\n"))
# Gets the users height and allocates it as a float point variable
height = float(input("How tall are you (in meters)?\n"))
# Gets the users weight and allocates it as a integer variable
weight = float(input("How much do you weigh (in kilograms)?\n"))
# Calculates the users bmi
heightSq = float(pow(height, 2))
bmi = float(round(weight / heightSq, 2))

healthStatus = input("Would you like to know your health status? (Please respond with Y or N)\n")

# Sets 0 as default to prevent the program breaking
strength = 0
lives = 0
energy = 0
# checks user wants to know health status
if healthStatus == "Y":
    # if statement to allocate values to lives and strength variables
    if 18.50 <= bmi <= 24.99:
        lives = 10
        strength = 6
    elif bmi < 18.50 or 25.00 <= bmi <= 29.99:
        lives = 6
    elif 25.00 <= bmi <= 29.99:
        strength = 8
    elif 30.00 <= bmi <= 34.99:
        print(bmi)
        lives = 4
        strength = 10
    elif bmi < 18.50:
        strength = 4

    # if statement to allocate values to the energy variable
    if age <= 10:
        energy = 10
    elif age <= 20:
        energy = 7
    elif age <= 40:
        energy = 5
    elif age <= 60:
        energy = 3

    # Output from if statements
    print(f"{name}'s Health Status\n\n"
          f"Lives:{lives * '❤'}\n"
          f"Energy: {energy * '▱'}\n"
          f"Strength: {strength * '💪'}\n")
