# first function to display the ladder using a parameter from the second function
def display_ladder(amount):
    for count in range(0, amount):
        check = amount - 1
        if count != check:
            print("| |\n"
                  "***")
        elif count == check:
            print("| |\n"
                  "***\n"
                  "| |")


# second function to get the users input amount
def create_ladder():
    steps = 0
    while steps == 0:
        steps = int(input("How many steps remain?\n"))
    display_ladder(steps)


# calls the user input function
create_ladder()
