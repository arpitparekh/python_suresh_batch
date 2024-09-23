from tkinter import *
from tkinter.font import Font
from turtle import width
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
root.title("My Windows")

myFont = Font(family="Helvetica", size=8, weight="bold",underline=True)

myVar = StringVar()
myVar.set("Hello From Tkinter This is a long text that will be justified within the label widget.")

label = Label(root,text="Hello From Tkinter This is a long text that will be justified within the label widget.", bg = "grey",font=myFont,width=30,height=10,anchor="e",justify="right",wraplength=70,relief="sunken",borderwidth=3,textvariable=myVar)
label.pack(pady=20)
# label.grid(column=0,row=0)
# label.place(x=10,y=20)

# image = Image("/home/arpit-parekh/Downloads/bascom_projects/python_suresh_batch/tkinter_class/cow.jpg")
try:
    # Replace this path with the actual path to your image
    image_path = "/home/arpit-parekh/Downloads/bascom_projects/python_suresh_batch/tkinter_class/cow.jpg"

    # Open the image file using PIL
    pil_image = Image.open(image_path)

    pil_image.thumbnail((200, 200))  # width and height

    # Convert PIL image to PhotoImage
    photo = ImageTk.PhotoImage(pil_image)

    # Create a new label with the image
    image_label = Label(root, image=photo,cursor="heart",text="Mooo",compound="top",font=myFont)
    # state="disabled"
    image_label.image = photo  # Keep a reference!
    image_label.pack()

except FileNotFoundError:
    print(f"Error: Image file not found at {image_path}")
except Exception as e:
    print(f"An error occurred: {e}")
# label2.grid(column=1,row=1)
# label2.place(x=30,y=30)



def clickFucntion():
  print("Button Clicked")
  print(entry.get())
  myVar.set("Click kiya re bhai, Click kiya re")

entry = Entry(root)
entry.pack()
button = Button(root,text="Click me",command=clickFucntion)
button.pack()

# pack()
# grid()
# place()

root.mainloop()


"""
# Tkinter Label Constructor Parameters

The Tkinter `Label` widget constructor accepts the following parameters:

1. `master`: The parent widget (required)
2. `text`: The text to display (string)
3. `font`: Text font (tuple or Font object)
4. `fg` or `foreground`: Text color
5. `bg` or `background`: Background color
6. `width`: Width of the label in characters (or pixels if bitmap/image is used)
7. `height`: Height of the label in lines of text (or pixels if bitmap/image is used)
8. `anchor`: Text position if label is larger than text (N, NE, E, SE, S, SW, W, NW, or CENTER)
9. `justify`: Multi-line text alignment (LEFT, CENTER, or RIGHT)
10. `wraplength`: Maximum number of characters per line for wrapping
11. `padx`: Horizontal padding
12. `pady`: Vertical padding
13. `relief`: Border style (FLAT, RAISED, SUNKEN, GROOVE, or RIDGE)
14. `borderwidth`: Border width
15. `textvariable`: StringVar object to update the label text dynamically
16. `image`: Image to display instead of text
17. `bitmap`: Bitmap to display instead of text
18. `compound`: Specifies how to display both text and image/bitmap (TOP, BOTTOM, LEFT, RIGHT, or CENTER)
19. `cursor`: Mouse pointer to display when over the widget
20. `takefocus`: If true, the widget accepts input focus
21. `highlightbackground`: Color of focus highlight when widget doesn't have focus
22. `highlightcolor`: Color of focus highlight when widget has focus
23. `highlightthickness`: Thickness of focus highlight
24. `state`: Widget state (NORMAL or DISABLED)
25. `underline`: Index of character to underline (-1 for none)

Note: Colors can be specified as names ("red", "blue", etc.) or as hexadecimal values ("#FF0000", "#0000FF", etc.).

import tkinter as tk
from tkinter import font as tkfont

root = tk.Tk()
root.title("Tkinter Label Examples")

# Basic label
label1 = tk.Label(root, text="Basic Label")
label1.pack(pady=5)

# Font
custom_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
label2 = tk.Label(root, text="Custom Font", font=custom_font)
label2.pack(pady=5)

# Colors
label3 = tk.Label(root, text="Custom Colors", fg="white", bg="blue")
label3.pack(pady=5)

# Width and Height
label4 = tk.Label(root, text="Fixed Width", width=20, bg="yellow")
label4.pack(pady=5)

# Anchor
label5 = tk.Label(root, text="Anchored Text", width=20, anchor="e", bg="lightgrey")
label5.pack(pady=5)

# Justify
long_text = "This is a long text that will be justified within the label widget."
label6 = tk.Label(root, text=long_text, wraplength=150, justify="center", bg="lightgreen")
label6.pack(pady=5)

# Padding
label7 = tk.Label(root, text="Padded Label", padx=20, pady=10, bg="pink")
label7.pack(pady=5)

# Relief and Border
label8 = tk.Label(root, text="Relief and Border", relief="raised", borderwidth=3)
label8.pack(pady=5)

# Text Variable
var = tk.StringVar()
var.set("Dynamic Text")
label9 = tk.Label(root, textvariable=var)
label9.pack(pady=5)

# Button to change dynamic text
tk.Button(root, text="Change Text", command=lambda: var.set("New Text")).pack()

# Image
img = tk.PhotoImage(file="path_to_image.png")  # Replace with actual image path
label10 = tk.Label(root, image=img)
label10.image = img  # Keep a reference
label10.pack(pady=5)

# Compound (Text and Image)
label11 = tk.Label(root, text="Text and Image", image=img, compound="left")
label11.image = img  # Keep a reference
label11.pack(pady=5)

# Cursor
label12 = tk.Label(root, text="Hover over me!", cursor="heart")
label12.pack(pady=5)

# State
label13 = tk.Label(root, text="Disabled Label", state="disabled")
label13.pack(pady=5)

# Underline
label14 = tk.Label(root, text="Underlined Text", underline=2)
label14.pack(pady=5)

root.mainloop()

"""


