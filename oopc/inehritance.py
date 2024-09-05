# inheritance
# varso
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):

  def __init__(self, name, age, marks):
    super().__init__(name, age)         # super is used to call parent class constructor
    self.marks = marks

  def display(self):
    print(self.name)
    print(self.age)
    print(self.marks)


s = Student("suresh",23,45)
s.display()


