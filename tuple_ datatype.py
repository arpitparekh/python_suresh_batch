t = (12,45,6,545,"Bascom",True)
# t[0] = 13   # tuple does not allow update
print(t)

print(t[-2])

print(t[:4])

myList = list(t)
myList.append(45)
print(myList)
t = tuple(myList)
print(t)

(a,b,c,d,e,f,g) = t  # unpacking

print(a)

(x,y,*z) = t
print(z)
print(type(z))

resultTuple = t * 2
print(resultTuple)
