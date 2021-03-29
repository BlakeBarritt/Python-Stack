# I had worked on this with the group code session yesterday and how we solved the User assignment was different than the outline. I understand the AttributeError means I didn't return an instance in the code. Went back and did the Assignment as shown in Methods and Attributes to do it correctly.

class User:
    def __init__(self, username):
        self.name = username
        self.accountBalance = 0
        
    def makeDeposit(self,amount):
        self.accountBalance += amount
        return self
    
    def makeWithdrawl(self, amount):
        self.accountBalance -= amount
        return self
    
    def displayUserBalance(self):
        print (f"User: {self.name} balance is: {self.accountBalance}")
        return self
        
guido = User("Guido Van Rossum")
monty = User("Monty Python")
blake = User("Blake")
        
guido.makeDeposit(150).makeDeposit(100).makeDeposit(100).displayUserBalance()
monty.makeDeposit(500).makeDeposit(500).makeWithdrawl(500).makeWithdrawl(500).displayUserBalance()
blake.makeDeposit(75).makeWithdrawl(25).makeWithdrawl(25).makeWithdrawl(25).displayUserBalance()

#//////////////////////////////////////////////////////////////////////////////////////////////   
# #Creating class User
# class User:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
    
#     #adding deposit method
#     def makeDeposit(self, amount):
#         self.balance += amount
    
#     #adding withdrawl method
#     def makeWithdrawl(self,amount):
#         self.balance -= amount
#     #adding display user balance
#     def userBalance(self):
#         print (self.balance)
        
#             # 2 arguments: name and starting account balance passed in
# guido = User("Guido Van Rossum", 150)
# monty = User("Monty Python", 500)
# blake = User("Blake", 0)

# Don't need self when calling function as it's implied. When we call on a method from an instance, that instance and all of its information is passed in as "self"

#//////////////////////////////// CHAINING METHODS ////////////////////////////////

# # First User make 3 desposits, 1 withdrawl and display balance
# guido.makeDeposit(150).makeDeposit(100).makeDeposit(100).userBalance()

# # Second user make 2 deposits, 2 withdrawls and display balance
# monty.makeDeposit(500).makeDeposit(500).makeWithdrawl(500).makeWithdrawl(500).userBalance()

# # Third user make 1 deposit, 3 withdrawls and display balance
# blake.makeDeposit(75).makeWithdrawl(25).makeWithdrawl(25).makeWithdrawl(25).userBalance()
