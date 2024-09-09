from abc import ABC, abstractmethod


class Car(ABC):   # kam chor boss
  def __init__(self, brand, model,year):
    self.brand = brand
    self.model = model
    self.year = year

  @abstractmethod
  def displayDetails():
    pass

  def start():
    print("Car started")

class BMW(Car):
  def displayDetails(self):
    print(self.brand)
    print(self.model)
    print(self.year)

class Mercedes(Car):
  def displayDetails(self):
    print(self.brand)
    print(self.model)
    print(self.year)

b = BMW("BMW","X5",2020)
b.displayDetails()

m = Mercedes("Mercedes","C200",2021)
m.displayDetails()
