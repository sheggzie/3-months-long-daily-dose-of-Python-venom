# Create a command-line interface (CLI) task manager.

# Features to implement:
# Add a task
# Remove a task
# List all tasks
# Store tasks in a file so they persist between program runs.

def tasker():
    end_prompt = ["end", "close", "stop", "exit", "quit"]    
    while True:    
        prompt = input("What would you like to do?: ").lower()
        if prompt.lower() in end_prompt:
            print("Ending loop...")
            break
        else:
            print(prompt)
tasker()