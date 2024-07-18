# Write a program that reads from a file and handles exceptions for file not found and other I/O errors.

def reader():
    try:
        with open("random.txt", "r") as file:
            line = file.readlines()
            for i in line:
                print(i.strip())
    except FileNotFoundError:
        print("File name 'random.txt' not found!")
    except IOError as e:
        print(f"An IO Error occured: {e}")
    except Exception as e:
        print(f"An error occured: {e}")
reader()        
