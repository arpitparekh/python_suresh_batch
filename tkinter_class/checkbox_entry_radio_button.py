from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Other Widgets")

# checkbox
var1 = IntVar()
var2 = IntVar()
box1 = Checkbutton(root,text="Male",variable=var1)
box1.pack()
box2 = Checkbutton(root,text="Female",variable=var2)
box2.pack()

# radio button
var = IntVar()

radio1 = Radiobutton(root,text="Cycling",variable=var,value=1)
radio2 = Radiobutton(root,text="Rowing",variable=var,value=2)
radio3 = Radiobutton(root,text="Boxing",variable=var,value=3)
radio4 = Radiobutton(root,text="Gaming",variable=var,value=4)

radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()

entry = Entry()
entry.pack()

def getData():

  if(var1.get()==1):
    print("Male")
  if(var2.get()==1):
    print("Female")

  if(var.get()==1):
    print("Cycling")
  if(var.get()==2):
    print("Rowing")
  if(var.get()==3):
    print("Boxing")
  if(var.get()==4):
    print("Gaming")

  print(entry.get())

button = Button(root,text="Click me",command=getData)
button.pack()

root.mainloop()
