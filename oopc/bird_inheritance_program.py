# Define two classes Bird with a method fly() and Fish with a method swim(). Derive a class Penguin from both Bird and Fish. In Penguin, override the fly() method to print "Penguins can't fly". Create an object of Penguin and call both fly() and swim().

# multiple inheritance

class Bird:
  def fly(self):
    print("Birds can fly")

class Fish:
  def swim(self):
    print("Fish can swim")

class Penguin(Bird,Fish):
  def fly(self):
    print("Penguins can't fly")

p = Penguin()
p.fly()
p.swim()
