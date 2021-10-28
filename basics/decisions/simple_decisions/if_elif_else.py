# user input for direction
direction = input("Which direction should I paint?")
# sets all the characters to lowercase so the if statement condition can be met
d = direction.lower()
# checks whether or not the user has inputted the correct string
if d == "up" or d == "down":
    direction = d + "ward"
elif direction.lower() == "right" or direction.lower() == "left":
    direction = d + "ward"
# prints output based on user input
print(f"I am painting in the {direction} direction!")