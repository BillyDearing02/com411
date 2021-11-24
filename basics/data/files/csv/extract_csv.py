# imports csv module
import csv


# extracts names from the csv file
def extract(f_path):
    print("Extracting...")
    with open(f_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        names = ""
        for values in csv_reader:
            # adds the csv names to the names variable
            names = names + values[1] + "\n"

        print(f"Done! The extracted names are as follows:\n{names}")


# basic run function
def run():
    f_path = "bots.csv"
    extract(f_path)


# runs the program
if __name__ == "__main__":
    run()
