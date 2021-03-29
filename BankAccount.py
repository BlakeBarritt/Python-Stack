class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount >= self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else: self.balance -= amount
        return self
    
    def display_account_info(self):
        print (f"Balance:{self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance >= 0:
            self.balance = (self.balance + self.balance * self.int_rate)
        else: print ("The yield interest is null")
        return self

account1 = BankAccount(.02, 0)
account2 = BankAccount(.02, 0)

account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest()
print(account1.balance)

account2.deposit(100).deposit(100).withdraw(100).withdraw(50).yield_interest()
print(account2.balance)
