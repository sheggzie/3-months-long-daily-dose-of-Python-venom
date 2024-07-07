# Write a program that reads data from a CSV file and processes it.
import csv

with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)