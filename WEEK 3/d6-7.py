# Bank Account System Project:
# Create a class-based bank account system.
# Features to implement:
# Create accounts (savings and checking)
# Deposit and withdraw money
# Transfer money between accounts
# Display account details

import random

class BankAccount:
    def __init__(self):
        self.AccountType = ''
        self.AccountBalance = 0
        self.AccountName = ''

    def create_account(self):
        print("What type of account do you want to create? ")
        print("Enter A for Savings account")
        print("Enter B for Checking account")

        prompt = input("Account type: ").capitalize()

        if prompt == "A":
            self.AccountType = "Savings"
        elif prompt == "B":
            self.AccountType = "Checking"
        else:
            print("Error! Enter a valid input.")        
        print(f"{self.AccountType} account selected!")
        
        self.name = input("Enter your name: ")
        self.acctnum = random.randint(1000000000, 9999999999)

        print(f"Hello {self.name}, your account with number: {self.acctnum} has been created successfully!")
    
    def deposit(self):
        print(f"Hello, how much do you want to deposit?")
        prompt = int(input("Enter amount: "))
        self.AccountBalance += prompt
        print(f"{prompt} deposited. Your new balance is {self.AccountBalance}")


newact = BankAccount()

while True:
    prompt = input("Enter a prompt: ")
    match prompt:
        case "create account":
            newact.create_account()
        case "deposit":
            newact.deposit()
        case "withdraw":
            pass
        case "end" | "close" | "quit":
            break
        case _:
            print("Error! Enter a valid prompt.")