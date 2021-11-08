# function that builds a dictionary and returns it when called
def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}

    return sequences

# function to start the program / outputs the dictionary by calling the first function
def run():
    print(pattern())


# calls the second function
run()
