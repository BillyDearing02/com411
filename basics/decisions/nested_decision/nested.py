
cover = input("What type of cover does the book have?\n")

# checks if the if statement condition has met
if cover.lower() == "soft":
    bound = input("Is the book perfect-bound?")
    # use of a nested if statement
    if bound.lower() == "yes":
        print(f"{cover} cover, perfect bound books are very popular!")
# else if in case the cover is hard
elif cover.lower() == "hard":
    print(f"Books with {cover} covers can be more expensive!")
