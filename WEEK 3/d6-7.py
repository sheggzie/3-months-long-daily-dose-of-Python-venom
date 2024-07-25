# Bank Account System Project:
# Create a class-based bank account system.
# Features to implement:
# Create accounts (savings and checking)
# Deposit and withdraw money
# Transfer money between accounts
# Display account details

import random, csv

filename = "database.csv"

class BankAccount:
    def __init__(self):
        self.AccountType = ''
        self.AccountBalance = 0

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

        with open(filename, "a", newline="") as file:
            db = csv.writer(file)
            db.writerow([self.name, self.acctnum, self.AccountBalance, self.AccountType])

        print(f"Hello {self.name}, your account with number: {self.acctnum} has been created successfully!")
    
    def deposit(self):
        print(f"Hello {self.name}, how much do you want to deposit?")
        prompt = int(input("Enter amount: "))
        self.AccountBalance += prompt
        
        rows = []
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:                
                if int(row[1]) == self.acctnum:
                    row[2] = str(self.AccountBalance)
                rows.append(row)
        
        with open(filename, "w", newline="") as file:
            db = csv.writer(file)
            db.writerows(rows)

        print(f"{prompt} deposited. Your new balance is {self.AccountBalance}")

    def withdraw(self):
        print(f"Hello {self.name}, how much do you want to withdraw?")
        prompt = int(input("Enter amount: "))
        if self.AccountBalance == 0 or self.AccountBalance < prompt:
            print("Insufficient funds!")
        else:
            self.AccountBalance -= prompt
                    
        rows = []
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:                
                if int(row[1]) == self.acctnum:
                    row[2] = str(self.AccountBalance)
                rows.append(row)
        
        with open(filename, "w", newline="") as file:
            db = csv.writer(file)
            db.writerows(rows)

        print(f"{prompt} withdrawn. Your new balance is {self.AccountBalance}")

newact = BankAccount()

while True:
    prompt = input("Enter a prompt: ")
    match prompt:
        case "create account":
            newact.create_account()
        case "deposit":
            newact.deposit()
        case "withdraw":
            newact.withdraw()
        case "end" | "close" | "quit":
            break
        case _:
            print("Error! Enter a valid prompt.")