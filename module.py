# modules
# user define module
# system define module

# import my_module as m
from my_module import MyClass,sum,mul
from array import array
import asyncio as asc   # used to create asynchronous functions
import base64 as b64
import calendar
from collections import Counter

obj = MyClass("Bascom")
obj.display()

print(sum(3,4))
print(mul(1,2))

# create an array
# array is collection of similar type of data  # numpy (numpy array)

numbers = array('i',[1,2,3,4,5])
print(numbers)
print(numbers[0])

# api call
# database operations


async def background():    # coroutine
  await asc.sleep(1)     # waiting explicitly
  print("Background task is running")

print("Start")
# background()
asc.run(background())   # to ru async function
print("End")


password = "bascom@123"
enCodedPassword = b64.b64encode(password.encode())
print(enCodedPassword)                                         # sha256

decodedPassword = b64.b64decode(enCodedPassword).decode()
print(decodedPassword)


cal =  calendar.month(2022,1)

print(cal)

name = "Bascom Bridge"
c = Counter(name)
print(c)
