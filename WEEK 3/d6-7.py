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

newact = BankAccount()
newact.create_account()
