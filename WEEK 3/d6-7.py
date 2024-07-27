# Bank Account System Project:
# Create a class-based bank account system.
# Features to implement:
# Create accounts (savings and checking)
# Deposit and withdraw money
# Transfer money between accounts
# Display account details

import random
import csv

filename = "database.csv"

print("Welcome to the S-Bank")

class BankAccount:
    def __init__(self):
        self.AccountType = ''
        self.AccountBalance = 0
        self.name = ''
        self.acctnum = None

    def login(self):
        print("A: create account")
        print("B: login")
        print("C: exit")
        prompt = input("Enter an option: ").capitalize()
        if prompt == "B":
            ask = input("Enter your account number: ").strip()
            with open(filename, "r") as file:
                read = csv.reader(file)
                for row in read:
                    if row[1] == ask:
                        self.name = row[0]
                        self.acctnum = int(row[1])
                        self.AccountBalance = int(row[2])
                        self.AccountType = row[3]
                        print(f"Hi {self.name}, Welcome to S-Bank!")
                        return True
                print("Account not found!")
                return False
        elif prompt == "A":
            return "create account"
        elif prompt == "C":
            print("Bye")
            return None
        else:
            print("Invalid option.")
            return False

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
            return
        
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

    def send_funds(self):
        beneficiary = input("Enter beneficiary's account number: ").strip()
        amount = int(input("Enter amount to send: "))

        if self.AccountBalance < amount or self.AccountBalance == 0:
            print("Insufficient funds!")
            return

        beneficiary_found = False
        rows = []

        with open(filename, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == beneficiary:
                    row[2] = str(int(row[2]) + amount)  # Add amount to beneficiary's balance
                    beneficiary_found = True
                elif row[1] == str(self.acctnum):
                    row[2] = str(int(row[2]) - amount)  # Deduct amount from sender's balance
                rows.append(row)

        if not beneficiary_found:
            print("Beneficiary account not found!")
            return

        with open(filename, "w", newline="") as file:
            db = csv.writer(file)
            db.writerows(rows)

        self.AccountBalance -= amount
        print(f"{amount} sent to account {beneficiary}. Your new balance is {self.AccountBalance}")

    def inquiry(self):
        print("Enter A to check balance.")
        print("Enter B to check account number.")
        prompt = input("Enter a prompt: ").capitalize().strip()
        if prompt == "A":
            print(f"Hello {self.name}, your current balance is {self.AccountBalance}")
        elif prompt == "B":
            print(f"Hello {self.name}, your account number is {self.acctnum}")
        else:
            print("Error! Enter a valid prompt.")


newact = BankAccount()

while True:
    action = newact.login()
    if action == "create account":
        newact.create_account()
    elif action == None:
        break
    elif action:
        prompt = input("Enter a prompt: ").lower()
        match prompt:
            case "deposit":
                newact.deposit()
            case "withdraw":
                newact.withdraw()
            case "send":
                newact.send_funds()
            case "inquiry":
                newact.inquiry()
            case "end" | "close" | "quit":
                break
            case _:
                print("Error! Enter a valid prompt.")
