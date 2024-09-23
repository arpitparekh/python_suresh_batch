
for i in range(1,8): # 1, 2, 3 ,4 ,5

  for j in range(1,8):
    print("* ",end="")

  print()

"""
1 *
2 **
3 ***
4 ****
5 *****

"""

print()

for i in range(1,6):
  for j in range(1,i+1):
    print("* ",end="")

  print()

print()

"""

*****
****
***
**
*

"""

for i in range(1,6):
  for j in range(1,7-i): # 1..6  1..5
    print("* ",end="")

  print()

print()


"""

     *
    **
   ***
  ****
 *****

"""

for i in range(1,6): # 2

  for k in range(1,6-i):
    print("  ",end="")

  for j in range(1,i+1):
    print("* ",end="")

  print()


print()

"""    practice

*****
 ****
  ***
   **
    *

"""
