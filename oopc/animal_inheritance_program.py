# Write a Python program to define a base class Animal with a method sound() that prints "Animals make sound". Derive a class Dog that overrides the sound() method to print "Dogs bark". Create an object of Dog and call the sound() method.


class Animal:  # base class
    def sound(self):
        print("Animals make sound")

class Dog(Animal) : # Dogs bark
  def sound(self):
        print("Dogs bark")


# when child class can access parent class methods and variables it calls

d = Dog()
d.sound()   # always prefer its own class method first
