1.Write a Python class BankAccount that manages a simple bank account with the following features: 
Requirements:
Initialize with account number, holder name, and initial balance (default 0)
Implement deposit(amount) method that adds money (must be positive)
Implement withdraw(amount) method that removes money (check sufficient balance)
Implement get_balance() method to return current balance
Implement transfer(amount, target_account) to transfer money to another account
Maintain transaction history (list of all transactions with type, amount, and timestamp)
Implement __str__() for readable representation

from datetime import datetime

class BankAccount:

  def __init__(self,account_number,holder_name,initial_balance=0):
   self.account_number=account_number
   self.holder_name=holder_name
   self.initial_balance=initial_balance
   self.transaction_history=[]

  def deposit(self,deposit):
   if deposit>0:
     self.initial_balance+=deposit
     self.transaction_history.append(("Deposit",deposit,datetime.now()))
     print("Balance after deposit of",deposit,"is",initial_balance)
   else:
     print("Deposit amount must be positive")

  def withdraw(self,withdrawal):
   if withdrawal>0:
     if self.initial_balance >=withdrawal:
      self.initial_balance-=withdrawal
      self.transaction_history.append(("Withdrawal",withdrawal,datetime.now()))
      print("Balance after withdrawal of",withdrawal,"is",initial_balance)
     else:
      print("No sufficient balance for withdrawal")
   else:
    print("Withdrawal amount must be positive")

  def get_balance(self):
   print("Balance of",holder_name,"for account number",account_number,"is",initial_balance)

  def transfer(self,amount,target_account):
    if amount>0:
     if self.initial_balance>=amount:
      self.initial_balance-=amount
      target_account.initial_balance+=amount
      self.transaction_history.append(("Transfer_out",amount,datetime.now()))
      target_account.transaction_history.append(("Transfer_in",amount,datetime.now()))
      print("Transfer successful")
     else:
      print("Insufficient balance")
    else:
     print("Transfer amount must be positive")

  def __str__(self):
    return f"Account Number: {self.account_number}, Holder: {self.holder_name}, Balance: {self.initial_balance}"
