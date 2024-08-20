# conditional
# condition will generate a flow of the program

# if

a = 55
if(a<30):
    print("a is less than 30")
else:
    print("a is greater than 30")
    
num = -34
if(num<0):
    print("number is negative")
else:
    print("number is positive")

# if number is divisible by 3 or not

num = 46
if(num%3==0):
    print("number is divisible by 3")
else:
    print("number is not divisible by 3")   
    
# if else ladder

marks = 35

if(marks <= 50 and marks >= 45):
    print("A grade")
elif(marks < 45 and marks >= 35): 
    print("B grade")   
elif(marks<35 and marks>=25):
    print("C grade")
else:
    print("Fail")
    
# nested if

number = 101

if(number%2==0):
    if(number<20):
        print("even and less than 20")
    else:
        print("even and greater than 20")
else:
    if(number<20):
        print("odd and less than 20")
    else:
        print("odd and greater than 20")   
        
# find greater number from 2 numbers

a = 55
b = 13                   

if(a<b):
    print(b,"is Greater")
else:
    print(a,"is Greater")
    

# find greater number from 3 numbers

a1 = 4599
b1 = 735
c1 = 166

if(a1>b1 and a1>c1):
    print(a1,"is greater")
elif(b1>c1):
    print(b1,"is greater")
else:
    print(c1,"is greater")
    
# match

day = 2

match day:
    case 1:
        print("day is 1")
    case 2:
        print("day is 2")
    case 3:
        print("day is 3")
        
# if(day==1):
#     print("day is 1")
# elif(day==2):
#     print("day is 2")                                