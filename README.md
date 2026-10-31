# personal_account
Personal Account Management System

Project Description

This project is a simple Personal Account Management System developed in Python. It simulates basic banking operations by allowing users to manage a personal bank account, perform deposits and withdrawals, check their current balance, and view transaction history.
The project demonstrates object-oriented programming (OOP) concepts in Python, including classes, objects, constructors, encapsulation, special methods, and operator overloading.

Features

Account Creation: Create a personal account with an account number and account holder's name.
Deposit Money: Deposit money into the account and update the balance.
Withdraw Money: Withdraw money if sufficient funds are available.
Balance Inquiry: Retrieve and display the current account balance.
Transaction History: View a history of deposits and successful withdrawals, including transaction types, amounts, and timestamps.
Account Information: Display the account number, account holder, and current balance.
Operator Overloading: Use the + operator to deposit money and the - operator to withdraw money.

Technologies Used

Python 3
datetime module for transaction timestamps

Project Structure

oop_assignment_3/
│
├── main.py
├── personal_account.py
└── README.md

Classes

1. Amount
The Amount class represents an individual financial transaction.

Attributes:

amount: The amount of money involved in the transaction.
timestamp: The date and time when the transaction occurred.
transaction_type: The type of transaction, either DEPOSIT or WITHDRAWAL.

Methods:

__init__(): Initializes a transaction.
__str__(): Returns a readable representation of the transaction.

2. PersonalAccount

The PersonalAccount class represents a personal bank account.

Attributes:

__account_number: The account's unique identifier.
__account_holder: The name of the account holder.
__balance: The current account balance, initialized to 0.0.
transactions: A list containing the account's transaction objects.

Methods:

__init__(): Initializes a new account.
deposit(amount): Deposits money and updates the balance.
withdraw(amount): Withdraws money if the amount is valid and sufficient funds are available.
get_balance(): Returns the current balance.
get_account_number(): Returns the account number.
set_account_number(account_number): Updates the account number.
get_account_holder(): Returns the account holder's name.
set_account_holder(account_holder): Updates the account holder's name.
print_transaction_history(): Displays the transaction history.
__str__(): Returns a readable summary of the account.
__add__(amount): Enables deposits using the + operator.
__sub__(amount): Enables withdrawals using the - operator.

Requirements

Python 3.8 or later
No external libraries are required.

How to Run

Clone or download this repository.
Open a terminal in the project directory.
Ensure the Python files are in the correct locations.

Run the main program:

python main.py

If your main Python file has a different name, replace main.py with its actual filename.

Usage Example

The following example demonstrates how to create an account, deposit money, withdraw money, check the balance, and display the transaction history.

from personal_account import PersonalAccount

# Create an account
acc1 = PersonalAccount(2240500, "Jane K")

# Display account information
print(acc1)

# Deposit money
acc1.deposit(1000)

# Withdraw money
acc1.withdraw(900)

# Display current balance
print(f"Current balance: {acc1.get_balance()}")

# Attempt a withdrawal with insufficient funds
acc1.withdraw(200)

# Perform additional transactions
acc1.deposit(500)
acc1.withdraw(350)

# Display updated balance
print(f"Current balance: {acc1.get_balance()}")

# Display transaction history
acc1.print_transaction_history()

Example Output

Account Number: 2240500
Account Holder: Jane K
Balance: 0.0

Deposit: 1000, New balance: 1000.0

Withdrawal: 900, New balance: 100.0

Current balance: 100.0

Insufficient funds. Current balance: 100.0

Deposit: 500, New balance: 600.0

Withdrawal: 350, New balance: 250.0

Current balance: 250.0

Transaction history: 
Transaction type: DEPOSIT, Amount: 1000, Timestamp: 2026-10-31 16:39:15
Transaction type: WITHDRAWAL, Amount: 900, Timestamp: 2026-10-31 16:39:16
Transaction type: DEPOSIT, Amount: 500, Timestamp: 2026-10-31 16:39:17
Transaction type: WITHDRAWAL, Amount: 350, Timestamp: 2026-10-31 16:39:18


Limitations

This project is intended for learning purposes and is not a production banking application.
Account data is stored in memory and is lost when the program terminates.
There is no database or persistent storage.
The program does not implement user authentication.
Currency formatting and currency conversion are not implemented.
Transaction records are maintained only during the current program session.


Author

Created as a Python programming assignment to practise object-oriented programming and basic account management.
