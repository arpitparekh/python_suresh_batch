# functions
# function is a block of code that runs when we called it
# functions are reusable code blocks

from segno import  *

# def keyword

def display():                              # function defination
  print("This is display function")


display()  # function call
display()  # function call
display()  # function call
display()  # function call
display()  # function call

# function consist of different parts

# function name
# function block
# function paramter
# function return type

def sum(a,b):
  print(a+b)

sum(12,14)
sum(10,11)
sum(20,22)
sum(24,1)
sum(1,1)


def printTable(num):
  for i in range(1,11):
    print(num,"x",i,"=",num*i)

printTable(10)
printTable(12)
printTable(99)
printTable(111)

# function return type

def myfunction():
  return 12

print(myfunction())

result = 10 + myfunction()

print(result)

sum(10,myfunction())

# function with parameter with return type

def mydata(x,y):
  return x*y

print(mydata(10,22))

sum(mydata(10,10),mydata(11,10))

################################################################


def fun(a,b):
  return a-b

def run(a,b,c):
  return a+b+c

def gun(x):
  return x*100

print(run(fun(10,20),gun(10),-50))

# def fun(a,b):
#   return a-b

fun2s = lambda a,b : a-b
print(fun2s(10,2))


##############################################
# function returning a fucntion

def another(a,b,c):
  return lambda a,b,c:a+b+c

print(another(12,13,14)(44,34,32))

# make qr code
qr = make_qr(content="https://pypi.org/project/segno/")
qr.save("qr.png")
