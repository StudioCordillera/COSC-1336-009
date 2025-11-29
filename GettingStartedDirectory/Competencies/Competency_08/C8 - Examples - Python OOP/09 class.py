class BankAccount(object):
    def __init__(self, initial_balance  = 0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def overdrawn(self):
        return self.balance < 0

my_account = BankAccount(100)
print("My initial Balance is ", my_account.balance)

my_account.withdraw(320)
my_account.deposit(125)

print("My now Balance is ",my_account.balance)
print(my_account.overdrawn())

if  my_account.overdrawn():
    print(" i am gone")
