# variables
# 1. variables are used to store values

_d = 12
d = 34
print(d)
print(_d)
# del d  remove datatype from memory

# datatypes
# int
num = 134
print(num)
print(type(num))

# float
num2 = 34434343434445.56
print(num2)
print(type(num2))

# complex number
com = 12 + 13j
print(com)
print(type(com))

# str
name = "Bascom"
print(name)
print(type(name))

# bool
is_admin = True
is_login = False
print(is_admin)
print(is_login)
print(type(is_admin))

# list group of values
fruits = ["apple", "banana", "cherry"]
numbers = [12,34,657,45,432,23]
print(fruits)
print(numbers)
print(type(fruits))

data = [1212,3.454,"Bascom",12 + 34j,[1,2,3]]
print(data)
print(type(data))

print(data[1])
data[2] = "tops"
print(data)

data.append(56.78)  # add data at the end of the list
print(data)

myList = [12,45,5,4,3,5,545]
print(myList)
myList[0:3] = [99,98,97]  # update an range of values
print(myList)

myList.insert(1,0)
print(myList)

mylist2 = [76,77,78,79]
myList.extend(mylist2)
print(myList)

myList.remove(0)
print(myList)
myList.pop(0)
print(myList)

myList.pop()
print(myList)

del myList[0]   # removing an element 
print(myList)

# myList.clear()
# print(myList)

print(len(myList))
# print(len(121212))  it will not take number

print(myList.sort(reverse = False))
print(myList)

myList.reverse()
print(myList)

extraList = myList.copy()
print(extraList)

anotherList = extraList
print(anotherList)

resultList = myList + anotherList
print(resultList)

print(resultList.count(97))
print(resultList.index(97))

print(resultList[-2])