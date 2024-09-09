# khayali pulav
# kamchor boss

# abstraction
# 1. abstract class
# 2. abstract method

# abstract class provide implementation to other class
# asbtract method is a method without any body
# you can not create object of abstract class

from abc import ABC, abstractmethod


class Boss(ABC):  # abstract class

  def fun():
    print("I am boss")

  @abstractmethod
  def work():      # self is not needed in abstract method
    pass

class Employee(Boss):

  def work(self):
    print("I am working")   # compulsary

e = Employee()
e.work()


