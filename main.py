#import the class PersonalAccount from the file personal_account
from personal_account import PersonalAccount

#create a test account assigning account number and holder
acc1 = PersonalAccount(2240500, "Jane K")
print(acc1)

#add money
acc1.deposit(1000)
#withdraw money
acc1.withdraw(900)
#check current balance
print(f"Current balance: {acc1.get_balance()}\n")
#withdraw money while exceeding the balance
acc1.withdraw(200)
acc1.deposit(500)
acc1.withdraw(350)

print(f"Current balance: {acc1.get_balance()}\n")
#check transaction_history
acc1.print_transaction_history()
