# Create a command-line interface (CLI) task manager.

# Features to implement:
# Add a task
# Remove a task
# List all tasks
# Store tasks in a file so they persist between program runs.

line_number = 0
lines = ''
def tasker():    
    def add_task(new_task, filename="task.txt"):
        
        with open(filename, "r") as file:
            global lines
            lines = file.readlines()
                        
        
        with open(filename, "a") as file:
            global line_number
            line_number = 1
            for i in lines:
                line_number += 1
            file.write(str(line_number) + ": " + new_task + "\n")

    def remove_task(item):  
        try:      
            with open("task.txt", "r") as file:
                lines = file.readlines()
                
            if item < 1:
                print(f"{item} is an invalid number, enter a number greater than or equal to 1")
            elif item > len(lines):
                print(f"Items in task is not up to {item}. Available items is {len(lines)}")
            elif item is type(str):
                print("Texts not supported! Please enter a number.")
                return
                
            del lines[item-1]

            with open("task.txt", 'w') as file:
                file.writelines(lines)
            print(f"Line number {item} has been deleted successfully!")
        except Exception as e:
            print(f"Oops! There was an error '{e}'!")

    def list_tasks():
        with open("task.txt", "r") as file:
            print(file.readlines())

    end_prompt = ["end", "close", "stop", "exit", "quit"]    
    while True:    
        prompt = input("What would you like to do?: ").lower()
        if prompt.lower() in end_prompt:
            print("Ending loop...")
            break
        elif prompt == "show tasks":
            list_tasks()
        elif prompt == "remove" or "Remove" or "delete" or "Delete":
            ask = int(input("Enter the line number to be deleted: "))
            remove_task(ask)
        else:
            add_task(prompt)
            print(prompt)
tasker()