# Write a program that reads a CSV file of product information and stores it in a list of dictionaries.
import csv


# brands = {
#     "brand": "apple",
#     "model": "iPhone 15",
#     "color": "black"
# }

def read_to_dict(filename="product info.csv"):
    brands = {}
    with open(filename, "r") as file:
        # rows = csv.reader(file)
        # for brand, model, color in rows:
        #     brands.update(brand)
    print(brands)

read_to_dict()
        