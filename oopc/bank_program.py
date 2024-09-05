class Bank:
  def __init__(self,name,balance):
    self.name = name
    self.balance = balance
  def deposit(self,amount):
    self.balance += amount
  def withdraw(self,amount):
    self.balance -= amount

  def display(self):
    print(self.name)
    print(self.balance)


b = Bank("John",1000)
b.deposit(500)
b.withdraw(200)
b.deposit(100)
b.withdraw(1000)
b.display()
