# defined function that displays an ASCII box with the user inputted word inside it.
def display_box(outWord):
    print(".---------------.\n"
          "|               |\n"
          f"|     {outWord}      |\n"
          "|               |\n"
          "'---------------'")


# defined function that displays the user inputted word in all lower case.
def display_lower(outWord):
    print(outWord.lower())


# defined function that displays the user inputted word in all upper case.
def display_upper(outWord):
    print(outWord.upper())


# defined function that displays the user inputted word and its reverse.
def display_mirror(outWord):
    charAmount = len(outWord)
    mirrored = ""
    for count in outWord:
        charAmount = charAmount - 1
        mirrored = mirrored + outWord[charAmount]

    print(f"{outWord} | {mirrored}")


# defined function that repeats the user inputted word based on how many times the user wants it to.
def display_repeat(outWord):
    # gets the amount of repeats
    repeatAmount = int(input("How many times do you want it to repeat?\n"))
    # loops until its gone through all the repeats.
    while repeatAmount > 0:
        # counts down the repeats.
        repeatAmount = repeatAmount - 1
        # checks if it is odd or even.
        if repeatAmount % 2:
            # calls lowercase function for even numbers.
            display_lower(outWord)
        else:
            # calls uppercase function for odd numbers.
            display_upper(outWord)


# defined function to begin the program.
def run():
    # gets the user inputted word.
    inpWord = input("Please enter a word.\n")
    # gets how the user wants it to be displayed.
    userDisplay = input("How would you like it to be displayed?\n")


    # if/elif statements to call the correct display function
    if "box" in userDisplay.lower():
        display_box(inpWord)
    elif "lower" in userDisplay.lower():
        display_lower(inpWord)
    elif "upper" in userDisplay.lower():
        display_upper(inpWord)
    elif "mirror" in userDisplay.lower():
        display_mirror(inpWord)
    elif "repeat" in userDisplay.lower():
        display_repeat(inpWord)

# begins the program
run()
