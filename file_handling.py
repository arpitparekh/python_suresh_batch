import os

# /home/arpit-parekh/files

f = open("/home/arpit-parekh/files/hello.txt","w")
f.write("From Suresh Batch")
f.close()

f1 = open("/home/arpit-parekh/files/hello.txt","r")
str =  f1.readline()
print(str)


for x in f1:
  print(x)
f1.close()

os.remove("/home/arpit-parekh/files/hello.txt")
