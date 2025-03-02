import json
import os


# Account class
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"


# Bank class
class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts
        self.load_from_file()  # Load accounts from file when the bank is initialized

    def create_account(self, name, initial_deposit):
        # Generate a unique account number
        account_number = len(self.accounts) + 1
        # Create a new account
        account = Account(account_number, name, initial_deposit)
        # Add the account to the dictionary
        self.accounts[account_number] = account
        print(f"Account created successfully! Account Number: {account_number}")
        self.save_to_file()  # Save accounts to file

    def view_account(self, account_number):
        # Retrieve the account from the dictionary
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found!")

    def deposit(self, account_number, amount):
        # Retrieve the account from the dictionary
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                print(f"Deposited {amount}. New balance: {account.balance}")
                self.save_to_file()  # Save accounts to file
            else:
                print("Invalid deposit amount!")
        else:
            print("Account not found!")

    def withdraw(self, account_number, amount):
        # Retrieve the account from the dictionary
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                print(f"Withdrew {amount}. New balance: {account.balance}")
                self.save_to_file()  # Save accounts to file
            else:
                print("Invalid withdrawal amount or insufficient balance!")
        else:
            print("Account not found!")

    def save_to_file(self):
        # Convert accounts to a dictionary format for JSON serialization
        accounts_data = {
            acc_num: {"name": acc.name, "balance": acc.balance}
            for acc_num, acc in self.accounts.items()
        }
        # Write accounts to a file
        with open("accounts.txt", "w") as file:
            json.dump(accounts_data, file)
        print("Accounts saved to file.")

    def load_from_file(self):
        # Check if the file exists
        if os.path.exists("accounts.txt"):
            # Load accounts from the file
            with open("accounts.txt", "r") as file:
                accounts_data = json.load(file)
            # Recreate Account objects from the loaded data
            for acc_num, data in accounts_data.items():
                self.accounts[int(acc_num)] = Account(int(acc_num), data["name"], data["balance"])
            print("Accounts loaded from file.")
        else:
            print("No accounts file found. Starting with an empty bank.")


# Main function to run the bank application
def main():
    bank = Bank()  # Initialize the bank

    while True:
        print("\nWelcome to the Bank Application!")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            bank.view_account(account_number)

        elif choice == "3":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "5":
            print("Thank you for using the Bank Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the application
if __name__ == "__main__":
    main()
