# Write a program that reads a CSV file of product information and stores it in a list of dictionaries.
import csv


def read_to_dict(filename="product info.csv"):
    brands = {}
    with open(filename, "r") as file:
        rows = csv.reader(file)
        for model, color in rows:
            brands[model] = color
    print(brands)
read_to_dict()        