from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Canvas")

canvas = Canvas(root, width=500, height=500,bg="lightblue")
canvas.pack()


canvas.create_rectangle(50, 50, 150, 100, fill="blue")

canvas.create_oval(200, 50, 300, 100, fill="red")

canvas.create_line(50, 200, 350, 220, fill="green", width=3)

canvas.create_text(200, 250, text="Hello, Canvas!", font=("Arial", 16))

root.mainloop()
