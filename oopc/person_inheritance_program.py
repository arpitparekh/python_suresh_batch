# Define a base class Person with a method display() that prints "I am a person". Derive a class Employee from Person that adds an attribute salary. Derive another class Manager from Employee that adds a method manage(). Create an object of Manager and call all methods.

class Person:
    def display(self):
        print("I am a person")

class Employee(Person):
    def __init__(self, salary):
        self.salary = salary

class Manager(Employee):

    def __init__(self, salary):
        super().__init__(salary)
    def manage(self):
        print("I am managing")

m = Manager(1000)
m.display()
m.manage()
print(m.salary)
