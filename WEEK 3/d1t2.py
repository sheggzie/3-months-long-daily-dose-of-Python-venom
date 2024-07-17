# Write a program that prompts the user for a number and raises an exception if the input is not a number.

def prompter():
    
    try:
        prompt = int(input("Enter a number: "))
        return prompt
    except ValueError:
        print("Error! Input has to be a number")
print(prompter())