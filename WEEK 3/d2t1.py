# Create a custom exception for invalid user input.


class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
def prompter():
    try:
        prompt = input("Enter a number: ")
        if not prompt.isdigit():
            raise CustomError("Error! Input must be a number.")
        return int(prompt)
    except CustomError as e:
        print(e)
prompter()
