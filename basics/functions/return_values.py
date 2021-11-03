# finds Beep and Bop's Weight based on user input
def weight():

    beWeight = float(input("What is the weight of Beep?\n"))
    boWeight = float(input("What is the weight of Bop?\n"))

    return beWeight, boWeight


def sum_weight(be, bo):
    sum = be + bo
    return sum


def calc_avg_weight(be, bo):
    avg = (be + bo) / 2
    return avg


def run():
    # sets the variables beep and bop to the user inputted weights
    beep, bop = weight()
    # asks the user to enter whether to calculate a sum or average
    calculate = input("What would you like to calculate (sum or average)?")
    if "sum" in calculate.lower():
        # allows for a dynamic print statement at the end
        calc = "sum"
        # gets the sum of the weight from the pre-defined function
        ans = sum_weight(beep, bop)
    elif "average" in calculate.lower():
        # allows for a dynamic print statement at the end
        calc = "average"
        # gets the average of the weight from the pre-defined function
        ans = calc_avg_weight(beep,bop)

    print(f"The {calc} of Beep and Bop's Weight is {ans}.")

# Runs the program
run()