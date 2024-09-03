# Create a class called 'Rectangle' with attributes 'length' and 'width'. Include methods to calculate the area and perimeter of the rectangle.

class Rectangle:
  def __init__(self,length,width):
    self.length = length
    self.width = width

  def findArea(self):
    print(self.length * self.width)

  def findPerimeter(self):
    print(2*(self.length + self.width))

r1 = Rectangle(10,20)
r1.findArea()
r1.findPerimeter()

r2 = Rectangle(30,40)
r2.findArea()
r2.findPerimeter()
