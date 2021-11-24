# imports the csv module
import csv


# opens the csv file and prints the headings and values
def read(f_path):
    with open(f_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}\nValues:")

        for values in csv_reader:
            print(values)


# basic run function
def run():
    # calls read function
    f_path = "bots.csv"
    read(f_path)


# begins the program
if __name__ == "__main__":
    run()
