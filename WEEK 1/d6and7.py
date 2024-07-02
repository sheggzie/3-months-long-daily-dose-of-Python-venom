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

    def remove_task(out):        
        with open("task.txt", "r") as file:
            lines = file.readlines()
            current_line = file.readline([out])
            print(current_line)
            
        # with open("task.txt", "w") as file:
        #     for line in lines:
        #         if line_number != out:
        #             file.write(str(line_number) + ": " + line + "\n")



    

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
        elif prompt == "remove":
            ask = str(input("Enter the line number to be deleted: "))
            remove_task(ask)
            # if ask in line_number:                
                # remove_task(ask)
                # print(type(line_number))
        else:
            add_task(prompt)
            print(prompt)
tasker()