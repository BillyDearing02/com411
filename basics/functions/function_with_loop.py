
# function with a loop and an if statement
def cross_bridge(step):
    for count in range(0, step):
        print("Crossed Step.")
    if step < 5:
        print("We must keep going!")
    else:
        print("The bridge is collapsing!")


# calls the function with different parameters to output a different response
cross_bridge(3)
cross_bridge(6)