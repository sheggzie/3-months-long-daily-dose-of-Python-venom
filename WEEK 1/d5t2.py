# Write a program to log messages to a file.

# Log messages to a file predefined as "log.txt" with the "filename" parameter.
def logger(message, filename="log.txt"):
    # Open file and append new messages to it and add a new line after each message.
    with open(filename, "a") as file:
        file.write(message + "\n")

logger("My name is Quadri, you can simply call me Sheggzie, preferably!")
logger("I am an aspiring Python developer/programmer.")
logger("I think coding is fun, only tiring if you encounter a bug, but yeah, be resilient, calm and try to fix it with help from online resources and you should be good :)")
logger("Thanks for reading this. Have fun. Bye :)")

print("Messages have been logged!")