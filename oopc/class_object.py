# oopc
# object oriented progrmaming concepts
# coding strcuture

# class
# class is blueprint
# class contains variables(atributes) and methods(member function)

class Student:
  name = ""
  age = 0
  gender = ""

  def display():
    print("This is display function")


# object
# object is instance of a class
# memomry container
# object is used to access class propoerties and function outside of a class


s = Student()   # create an object of Student class
s.name = "yash"
s.age = 22
s.gender = "male"
print(s.name)
print(s.age)
print(s.gender)

# s.display()

s1 = Student()
s1.name = "suresh"
s1.age = 22
s1.gender = "male"
print(s1.name)
print(s1.age)
print(s1.gender)

# s1.display()

