# gets the users adventure type
adventure = input("What type of adventure should I have?\n")
# checks adventure type and outputs the appropriate response
if ("short" in adventure.lower()) or ("scary" in adventure.lower()):
    print("Entering the dark forest!")
elif ("safe" in adventure.lower()) or ("long" in adventure.lower()):
    print("Taking the safe route!")
# in case an alternate input is used
else:
    print("Not sure which route to take.")