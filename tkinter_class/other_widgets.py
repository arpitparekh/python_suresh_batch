from tkinter import *
from tkinter.ttk import Progressbar
from tracemalloc import start
from tkinter.messagebox import *

root = Tk()
root.geometry("600x600")
root.title("Other Widgets")

# other widgets list
# list box
list = Listbox(root)
list.pack()

list.insert(1, "Python")
list.insert(2, "Java")
list.insert(3, "NodeJS")
list.insert(4, "MySQL")
list.insert(5, "MongoDB")

# Option menu
"""
Creates an OptionMenu widget that allows the user to select from a list of programming languages. The selected value is stored in the `var` StringVar.
"""
var = StringVar()
var.set("Python")
w = OptionMenu(root, var, "Python", "Java", "NodeJS", "MySQL", "MongoDB")
w.pack()

# progress bar with direction also
bar = Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')
# set custom progress
# i want to mannulay set the progress after some interval

# make a for loop that will set the progress with some time interval

# its stopiing in whole program

# for i in range(100):
#   time.sleep(0.1)
#   bar["value"] = i

# do this progress stull background so that is will not block my whole program

bar["maximum"] = 100
bar["value"] = 0

def start_progress():
  bar.start(10)

def stop_progress():
  bar.stop()

bar.pack()

Button(root,text="Start",command=start_progress).pack()
Button(root,text="Stop",command=stop_progress).pack()

# spinbox

spin = Spinbox(root,from_=0,to=100)
spin.pack()

# scale

scale = Scale(root,from_=0,to=100,orient=HORIZONTAL)
scale.pack()

# message box copy of label

message = Message(root,text="Hello")
message.pack()

# messagebox

def showbox():
  showwarning(title="Do you want to close this app",message="Bhai su kam close kare che ? Ram nathi tara ma gareeb")
  # showinfo
  # showerror
  


button = Button(root,text="Click Me",command=showbox)
button.pack()


root.mainloop()
