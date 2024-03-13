# Modify the withdraw method of BankAccount so that the bank
# account can not have a negative balance.
#
# If a person tries to withdraw more than what is in the
# balance, then the method should raise a ValueError.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return ValueError
        else:
            self.balance -= amount
            return self.balance

    def deposit(self, amount):
        self.balance += amount

bankaccount = BankAccount(200)
print(bankaccount.withdraw(80))





        # If the amount is more than what is in
        # the balance, then raise a ValueError
