# defines sight as a string variable
sight = ""
# function with a nested if to check
def checkStatus(status):
    # checks if the condition has been met
    if "a large boulder" in status.lower():
        print("\nIt's time to run!")
    else:
        print("\nWe will be fine.")

# while loop to continuously ask the user for an input
while sight == "":
    sight = input("What lies before us?\n")
# calls the pre-defined function
checkStatus(sight)

