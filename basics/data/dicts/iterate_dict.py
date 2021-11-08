# function to print all the keys in the dictionary
def display_keys(k):
    print("\nKeys:")
    for k in k.keys():
        print(k)


# function to print all the values in the dictionary
def display_values(v):
    print("\nValues:")
    for v in v.values():
        print(v)


# function to print all the items in the dictionary
def display_items(i):
    print("\nPairs:")
    for k, v in i.items():
        print(f"{k}: {v}")


# initial function to run the program
def run():
    # defines the dictionary
    sequences = {'Short Sequence': 3, 'Medium Sequence': 2, 'Long Sequence': 1}
    # prints what the dictionary is
    print(f"Dictionary:\n {sequences}")

    # calls each function
    display_keys(sequences)
    display_values(sequences)
    display_items(sequences)

# calls run function to begin the program
run()