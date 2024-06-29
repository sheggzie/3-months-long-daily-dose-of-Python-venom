# Create a script to read a text file and count the number of lines.

# Function to read the count of lines, takes the document name to be read as parameter
def count_lines(doc):
    # Open file as a readable format
    with open(doc, "r") as file:
        # Read each line in the file with the readlines() function
        lines = file.readlines()
        line_count = 0

        # Increment the value of variable "line_count" for each line read
        for line in lines:
            line_count += 1
        print(line_count)
count_lines("random.txt")