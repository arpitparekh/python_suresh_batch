mySet = {1,2,4,6,7,"Bascom",True,56}
anotherSet = {3,6,89,9,7,5,444,3,3,3,55} # hascode
j = {12,3,4,65,6,7}

print(mySet | anotherSet | j)

print(mySet)
mySet.discard("Bascom12")
print(mySet)
 
# duplicate not allowed
# unordered
# unchangable
print(mySet)
print(anotherSet)

f =  input("Please Enter Value : ")
print(f)

var = 45

print("Value is",var," he"," hello",sep=",",end="")

t1 = {1,2,3,4,5}
t2 = {4}

print(t1.intersection(t2))
print(t1)
print(t1.difference(t2))

print(t1.isdisjoint(t2))