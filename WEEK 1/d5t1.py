# Create a script to read a text file and count the number of lines.

with open("random.txt", "r") as file:
    lines = file.readlines()
    counts = 0

    for line in lines:
        counts += 1

print(counts)