# polymorphism
# poly (many)  morphism (forms)

# method overloading # python does not support method overloading
# method overriding


from typing import override


class Animal:
  def speak(self):
    print("Animal speaks")

  def speak(self):             # this replace all the previous speak function
    print("Dog barks")

a = Animal()
a.speak()

class Dog(Animal):
  def speak(self):              # method overriding
    print("Dog is Barking")

class Cat(Animal):
  def speak(self):
    print("Cat meows")

class Cow(Animal):
  def speak(self):
    print("Cow moo")


d = Dog()
# d.speak()

c = Cat()
# c.speak()

co = Cow()
# co.speak()

list = [d,c,co]

for i in list:
  i.speak()

def myPrint(x,y,z=0):     # method overloading
  print(x,y,z)

myPrint(1,2,3)
myPrint(9,8)
