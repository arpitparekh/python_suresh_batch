class Car:

  # atributes
  name = ""
  color = ""
  price = 0.0
  model = ""

  def intializeValue(self,name,color,price,model):
    self.name = name
    self.color = color
    self.price = price
    self.model = model

  def printvalues(self):
    print(self.name)
    print(self.color)
    print(self.price)
    print(self.model)


c = Car()
c.intializeValue("BMW","Black",1000000,"2020")
c.color = "Red"
c.printvalues()

c1 = Car()
c1.intializeValue("Audi","White",2000000,"2021")
c1.printvalues()

