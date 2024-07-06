# Write a program that writes user input to a file.

def writer(filename="d3t2.txt"):
    with open(filename, "a") as file:
        txt = input("type something here: ")
        file.write(txt + "\n")
        print(f"You added the text '{txt}' to {filename}")
writer()        