# encapsulation # store something inside a capsule

class Myclass:
  def __init__(self,a,b,c):   # parameterized contructor
    self.a = a
    self._b = b   # protected  (only access in child class)
    self.__c = c  # private members

  def display(self):
    print(self.a)
    print(self._b)
    print(self.__c)

class YourClass(Myclass):

  # def __init__(self,a,b,c):
  #   super().__init__(a,b,c)     # this is compulsary

  def hello(self):
    print("hello")
    print(self.a)
    print(self._b)
    print(self.__c)  # noit possible

# class Circle:
#   def __init__(self,radius):
#     self.radius = radius

#   def area(self):
#     print(3.14*self.radius*self.radius)

# c = Circle(10)
# c.area()

m = Myclass(10,2,3)
m.display()

yc = YourClass(1,2,3)
yc.hello()
