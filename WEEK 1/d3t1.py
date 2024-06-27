# Create a function to check if a number is a prime number.

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a Prime number!")
                return False
        print(f"{num} is a Prime number")
        return True
        
prime(53)



