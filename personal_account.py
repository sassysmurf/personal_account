
#this file contains a solution to the Personal Account Management task.

# Objective:
# In this assignment, I will create a Python program to manage a personal bank account.
# I will implement two classes, Amount and PersonalAccount, to handle transactions,
# track balances, and maintain a transaction history.

# Requirements:

# 1. Amount Class

# Create a class called Amount to represent a transaction amount. This class should include:
# Attributes:
# amount (float): The transaction amount.
# timestamp (datetime): The transaction date and time.
# transaction_type (str): A string indicating the type of transaction ('DEPOSIT'
# or 'WITHDRAWAL').

from datetime import datetime

class Amount:
# Methods:
# A constructor (__init__) to initialize the amount, timestamp and transaction_type.
    def __init__(self, amount, timestamp, transaction_type):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

# __str__(self) : Provides a string representation of the object for easier
# readability when printed or converted to a string.
    def __str__(self):
        return (f"Transaction type: {self.transaction_type}, Amount: {self.amount},"
                f"Timestamp: {self.timestamp} ")

# 2. PersonalAccount Class

# Create a class called PersonalAccount to represent a personal bank account.
# This class should include:
# Attributes:
# account_number (int): A unique identifier for the account.
# account_holder (str): The name of the account holder.
# balance (float): The current balance in the account.
# transactions (list): A list to store Amount objects representing deposit and
# withdrawal transactions.

class PersonalAccount:
# Methods:
# A constructor (__init__) to initialize account_number, account_holder, and
# set the initial balance to 0.0.
    def __init__(self, account_number, account_holder):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = 0.0
        self.transactions = []


# deposit(self, amount): A method to deposit money into the account. This method should:
# Create an Amount object with the 'DEPOSIT' type.
# Add the transaction to the transactions list.
# Update the balance.
    def deposit(self, amount):
        transaction = Amount(amount, datetime.now(), "DEPOSIT")
        self.transactions.append(transaction)
        self.__balance = self.__balance + amount
        print(f"Deposit: {amount}, New balance: {self.__balance}\n")

# withdraw(self, amount): A method to withdraw money from the account. This method should:
# Create an Amount object with the 'WITHDRAWAL' type.
# Add the transaction to the transactions list.
# Update the balance. Ensure that the withdrawal amount does not exceed
# the current balance.
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

            transaction = Amount(amount, datetime.now(), "WITHDRAWAL")
            self.transactions.append(transaction)

            print(f"Withdrawal: {amount}, New balance: {self.__balance}\n")

        else:
            print(f"Withdrawal: {amount}, Not enough balance: {self.__balance}\n")

# print_transaction_history(self): A method to print the transaction history
# of the account. Iterate through the transactions list and display each transaction,
# including the transaction_type and amount.
    def print_transaction_history(self):
     print(f"Transaction History:")
     for trs in self.transactions:
         print(trs)

# get_balance(self): A method to retrieve the current balance of the account.

    def get_balance(self):
        return self.__balance

# get_account_number(self): A method to retrieve the account number.
    def get_account_number(self):
        return self.__account_number

# set_account_number(self, account_number): A method to set the account number.
    def set_account_number(self, account_number):
        self.__account_number = account_number

# get_account_holder(self): A method to retrieve the account holder's name.
    def get_account_holder(self):
        return self.__account_holder
# set_account_holder(self, account_holder): A method to set the account holder's name.
    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

# __str__(self): Provides a string representation of the object for easier
# readability when printed or converted to a string.
    def __str__(self):
        return (f"Account Number: {self.__account_number}\n"
                f"Account Holder: {self.__account_holder}\n"
                f"Balance: {self.__balance}\n")
# __add__(self, amount): Performs the same operation as the deposit(self, amount)
# method, allowing for addition of the specified amount to the object.
    def __add__(self, amount):
        self.deposit(amount)
        return self
# __sub__(self, amount): Performs the same operation as the withdraw(self, amount)
# method, allowing for subtraction of the specified amount to the object.
    def __sub__(self, amount):
        self.withdraw(amount)
        return self
