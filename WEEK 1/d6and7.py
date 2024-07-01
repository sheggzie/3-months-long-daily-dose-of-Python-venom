# Create a command-line interface (CLI) task manager.

# Features to implement:
# Add a task
# Remove a task
# List all tasks
# Store tasks in a file so they persist between program runs.

def tasker():
    def add_task(new_task, filename="task.txt"):
        
        with open(filename, "r") as file:
            lines = file.readlines()
                        
        
        with open(filename, "a") as file:
            line_number = 1
            for i in lines:
                line_number += 1
            file.write(str(line_number) + ": " + new_task + "\n")

    def remove_task():
        pass

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
        else:
            add_task(prompt)
            print(prompt)
tasker()