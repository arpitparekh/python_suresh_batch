# loops in python
# repetative task and sequence task

# while loop
# for loop

# breaking statements
# break
# continue
# pass

# while loop
from numpy import char


num = 12
while(num>1):  # while loop iterate untill condition is true
  print(num)
  num = num-1 # 11 10 9 8 7 6 5 4 3 2

# # print 1 to 10 using while loop
# data = 1 # 2


# # please enter a number
# data = 1
# limit = int(input("Enter data"))  # 10
# while(data<=limit):
#   print(data)
#   data = data+1 # 2

# for loop
for i in range(1,11):
  print(i)    # i is a local variable of this loop

for ab in range(65,91):
  print(chr(ab))

for i in range(1,11,2):
  print(i)

for i in range(1,1001):
  if i%5==0:
    print(i)

# give me practice loop programs
# 1 to 100
# 1 to 50
# 50 to 1
# more complex questions

# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# 8 * 6 = 48
# 8 * 7 = 56
# 8 * 8 = 64
# 8 * 9 = 72
# 8 * 10 = 80

k = int(input("Enter Number to Print its table :  "))
for num in range(1,11):
  print(f"{k} * {num} = {num*k}")

list = [21,34,56,45,3,53656]

for i in list:
  print(i)

sum = 0 # 1 # 3 # 6
for i in range(1,11):
  sum = sum+i

print(f"Sum is {sum}")
