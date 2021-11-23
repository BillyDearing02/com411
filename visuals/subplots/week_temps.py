import csv


def read_data():

    with open("temps.csv", mode="r") as file:
        reader = csv.reader(file)
        headings = next(reader)
        for i in reader:



# def run():


read_data()
