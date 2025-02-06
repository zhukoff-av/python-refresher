class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


bank1 = BankAccount('User', 100)
bank1.deposit(100)
bank1.deposit(100)
bank1.withdraw(400)
print(bank1.balance)

bank2 = BankAccount('User', 77)
print(bank2.balance)
