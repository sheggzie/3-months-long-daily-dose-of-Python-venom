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
        self.account_type = ''
        self.account_balance = 0
        self.name = ''
        self.acctnum = None

    def login(self):
        print("A: Create account")
        print("B: Login")
        print("C: Exit")
        prompt = input("Enter an option: ").capitalize().strip()
        if prompt == "B":
            ask = input("Enter your account number: ").strip()
            try:
                with open(filename, "r") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[1] == ask:
                            self.name = row[0]
                            self.acctnum = int(row[1])
                            self.account_balance = int(row[2])
                            self.account_type = row[3]
                            print(f"Hi {self.name}, Welcome to S-Bank!")
                            return True
                print("Account not found!")
                return False
            except FileNotFoundError:
                print("Database file not found!")
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

        prompt = input("Account type: ").capitalize().strip()

        if prompt == "A":
            self.account_type = "Savings"
        elif prompt == "B":
            self.account_type = "Checking"
        else:
            print("Error! Enter a valid input.")
            return
        
        print(f"{self.account_type} account selected!")
        
        self.name = input("Enter your name: ").strip()
        self.acctnum = random.randint(1000000000, 9999999999)

        with open(filename, "a", newline="") as file:
            db = csv.writer(file)
            db.writerow([self.name, self.acctnum, self.account_balance, self.account_type])

        print(f"Hello {self.name}, your account with number: {self.acctnum} has been created successfully!")
    
    def update_account_balance(self):
        rows = []
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[1]) == self.acctnum:
                    row[2] = str(self.account_balance)
                rows.append(row)
        
        with open(filename, "w", newline="") as file:
            db = csv.writer(file)
            db.writerows(rows)

    def deposit(self):
        try:
            print(f"Hello {self.name}, how much do you want to deposit?")
            prompt = int(input("Enter amount: ").strip())
            self.account_balance += prompt
            self.update_account_balance()
            print(f"{prompt} deposited. Your new balance is {self.account_balance}")
        except ValueError:
            print("Invalid amount entered.")

    def withdraw(self):
        try:
            print(f"Hello {self.name}, how much do you want to withdraw?")
            prompt = int(input("Enter amount: ").strip())
            if self.account_balance == 0 or self.account_balance < prompt:
                print("Insufficient funds!")
            else:
                self.account_balance -= prompt
                self.update_account_balance()
                print(f"{prompt} withdrawn. Your new balance is {self.account_balance}")
        except ValueError:
            print("Invalid amount entered.")

    def send_funds(self):
        try:
            beneficiary = input("Enter beneficiary's account number: ").strip()
            amount = int(input("Enter amount to send: ").strip())

            if self.account_balance < amount or self.account_balance == 0:
                print("Insufficient funds!")
                return

            beneficiary_found = False
            rows = []

            with open(filename, "r", newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == beneficiary:
                        row[2] = str(int(row[2]) + amount)
                        beneficiary_found = True
                    elif row[1] == str(self.acctnum):
                        row[2] = str(int(row[2]) - amount)
                    rows.append(row)

            if not beneficiary_found:
                print("Beneficiary account not found!")
                return

            with open(filename, "w", newline="") as file:
                db = csv.writer(file)
                db.writerows(rows)

            self.account_balance -= amount
            print(f"{amount} sent to account {beneficiary}. Your new balance is {self.account_balance}")
        except ValueError:
            print("Invalid amount entered.")

    def inquiry(self):
        print("Enter A to check balance.")
        print("Enter B to check account number.")
        prompt = input("Enter a prompt: ").capitalize().strip()
        if prompt == "A":
            print(f"Hello {self.name}, your current balance is {self.account_balance}")
        elif prompt == "B":
            print(f"Hello {self.name}, your account number is {self.acctnum}")
        else:
            print("Error! Enter a valid prompt.")

newact = BankAccount()

while True:
    action = newact.login()
    if action == "create account":
        newact.create_account()
    elif action is None:
        break
    elif action:
        prompt = input("Enter a prompt: ").lower().strip()
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
