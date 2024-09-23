# constrcutor
# constrcutor is used to initialize the class
# constrcutor is type of function
# constrcutor calls automatically when we can create an object of class
# constrcutor and class name is same
# construcor is used to create an object of class

class Institute:
  def __init__(self,name,no_student,location):
    self.name = name
    self.no_student = no_student
    self.location = location

  def display(self):
    print(self.name)
    print(self.no_student)
    print(self.location)

i = Institute("Bascom",20,"Chandigarh")
i.display()
i2 = Institute("Bascom2",30,"Ahmedabad")
i2.display()
