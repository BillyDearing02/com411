# inputs for beep's health statuses formatted to integer variables
lives = int(input("Please enter the number of lives\n"))
energy = int(input("Please enter the energy level\n"))
shield = int(input("Please enter the shield level\n"))

# output of beep's health status based on user input
print("Health has been set.\n\n"
      
      f"Lives:  {lives * '❤'}\n"
      f"Energy: {energy * '▱'}\n"
      f"Shield: {shield * '🛡️'}\n")