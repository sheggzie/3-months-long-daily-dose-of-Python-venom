# Create a command-line interface (CLI) task manager.

# Features to implement:
# Add a task
# Remove a task
# List all tasks
# Clear saved tasks
# Store tasks in a file so they persist between program runs.

lines = ''
def tasker():
    print("Hello! Welcome to your CLI task manager.")
    print("Below are some helpful tips you might need!")
    print("To add a task, just enter the task e.g 'Make coffee after exercise'")
    print("To see your previously added available tasks, simply type 'show tasks'")
    print("To delete a task from list, enter 'remove' or 'delete', then enter the task number/ID to delete it")
    print("To clear the whole contents of a task, simply type 'clear tasks'")
    print("To close or exit once you're done, simply enter 'end' or 'exit' or 'close' or 'stop' or 'quit'")
    print("Have fun tasking :)")
    print("Loading...")
    print("Starting...")
    print("Shoot!!!")    
    def add_task(new_task, filename="task.txt"):
        
        with open(filename, "r") as file:
            global lines
            lines = file.readlines()
                        
        
        with open(filename, "a") as file:
            file.write(new_task + "\n")
        
        print(f"New task '{new_task}' has been added to your task list")

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

    def clear_tasks():
        with open("task.txt", "w") as file:
            file.truncate()
    
    while True:        
        prompt = input("What would you like to do?: ").lower()              
        match prompt:
            case "end" | "close" | "stop" | "exit" | "quit":
                print("Closing...")
                break
            case "show tasks":
                list_tasks()
            case "remove" | "delete":
                try:
                    ask = int(input("Enter the line number to be deleted: "))
                    remove_task(ask)
                except Exception as e:
                    print(f"Oops! There was an error '{e}'")
            case "clear tasks":
                try:
                    confirmation = str(input("Are you sure you want to clear all saved tasks? y/n: "))
                    if confirmation == "y":
                        clear_tasks()
                        print("All tasks have been cleared successfully!")
                        break
                    elif confirmation == "n":
                        break
                except Exception as e:
                    print(f"Oops! An error '{e}' occured")
            case _:
                add_task(prompt)
tasker()