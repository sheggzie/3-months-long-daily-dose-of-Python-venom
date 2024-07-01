# Create a command-line interface (CLI) task manager.

# Features to implement:
# Add a task
# Remove a task
# List all tasks
# Store tasks in a file so they persist between program runs.

def tasker():
    def add_task(new_task, filename="task.txt"):
        with open(filename, "a") as file:
            file.write(new_task + "\n")

    def remove_task():
        pass

    def list_tasks():
        pass

    end_prompt = ["end", "close", "stop", "exit", "quit"]    
    while True:    
        prompt = input("What would you like to do?: ").lower()
        if prompt.lower() in end_prompt:
            print("Ending loop...")
            break
        else:
            add_task(prompt)
            print(prompt)
tasker()