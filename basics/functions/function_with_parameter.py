# function to check what parameter has been put through
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Let's go deeper!")


# calls the function with different parameters
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")