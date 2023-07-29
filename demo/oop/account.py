class InsufficientFundsError (Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f"Insufficient balance {self.balance} for withdraw of {self.amount}"


class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFundsError(amount, self.balance)

        self.balance -= amount

    def getbalance(self):
        return self.balance

    def __str__(self):
        return f"{self.acno} - {self.ahname} - {self.balance}"

    def __eq__(self, other):
        return self.acno == other.acno

    def __gt__(self, other):
        return self.balance > other.balance


a1 = SavingsAccount(1, "Jack", -10000)
a1.withdraw(20000)

a2 = SavingsAccount(2, "Cathy")
a1.deposit(-10000)
a1.withdraw(5000)
print(a1.getbalance())
a2.deposit(50000)
