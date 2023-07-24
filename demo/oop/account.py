class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getbalance(self):
        return self.balance


a1 = SavingsAccount(1, "Jack", 10000)
a2 = SavingsAccount(2, "Cathy")
a1.deposit(10000)
a1.withdraw(5000)
print(a1.getbalance())
a2.deposit(50000)
