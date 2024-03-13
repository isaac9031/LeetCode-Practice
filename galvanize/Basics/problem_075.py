# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        

bankaccount = BankAccount(100)
bankaccount.deposit(60)
bankaccount.deposit(40)
print(bankaccount.get_balance())
bankaccount.withdraw(150)
print(bankaccount.get_balance())
