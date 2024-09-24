from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("User Form")

class UserFrom:
  def __init__(self,root):
    self.frame = Frame(root)
    self.frame2 = Frame(root)
    self.userNameEntry = Entry(self.frame)
    self.emailEntry = Entry(self.frame)
    self.passwordEntry = Entry(self.frame)
    self.addressEntry = Entry(self.frame2)
    self.phoneEntry = Entry(self.frame2)
    self.ageEntry = Entry(self.frame2)

  def createFirstFrame(self):
    userName = Label(self.frame, text="Username")
    userName.pack(padx=5,pady=5)

    self.userNameEntry.pack(padx=5,pady=5)

    email = Label(self.frame, text="Email")
    email.pack(padx=5)

    self.emailEntry.pack(padx=5,pady=5)

    password = Label(self.frame, text="Password")
    password.pack(padx=5)

    self.passwordEntry.pack(padx=5,pady=5)

    self.frame.pack(side=LEFT,padx=20,pady=20)

  def createSecondFrame(self):
    address = Label(self.frame2, text="Address")
    address.pack(padx=5,pady=5)

    self.addressEntry.pack(padx=5,pady=5)

    phone = Label(self.frame2, text="Phone")
    phone.pack(padx=5,pady=5)

    self.phoneEntry.pack(padx=5,pady=5)

    age = Label(self.frame2, text="Age")
    age.pack(padx=5,pady=5)

    self.ageEntry.pack(padx=5,pady=5)

    self.frame2.pack(side=RIGHT,padx=20,pady=20)


masterFrame = Frame(root)
masterFrame.pack()

form = UserFrom(masterFrame)

form.createFirstFrame()
form.createSecondFrame()

def getData():
  userName = form.userNameEntry.get()
  email = form.emailEntry.get()
  password = form.passwordEntry.get()
  address = form.addressEntry.get()
  phone = form.phoneEntry.get()
  age = form.ageEntry.get()
  label.configure(text=f"Name : {userName}\n Email : {email}\n  Password : {password}\n Address :{address}\n Phone : {phone}\n Age : {age}")

  print(userName)
  print(email)
  print(password)
  print(address)
  print(phone)
  print(age)

button = Button(root,text="Click Me",command=getData)
button.pack()

label = Label(root,text="")
label.pack()

root.mainloop()

