import tkinter as tk
import random

def create_gradient(canvas, x1, y1, x2, y2, color1, color2):
    for i in range(y1, y2):
        r = int(color1[0] + (float(i-y1)/(y2-y1)) * (color2[0]-color1[0]))
        g = int(color1[1] + (float(i-y1)/(y2-y1)) * (color2[1]-color1[1]))
        b = int(color1[2] + (float(i-y1)/(y2-y1)) * (color2[2]-color1[2]))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(x1, i, x2, i, fill=color)

def draw_mountain(canvas, x1, y1, x2, y2, color):
    canvas.create_polygon(x1, y1, x2, y1, (x1+x2)/2, y2, fill=color, outline=color)

def draw_tree(canvas, x, y, size):
    trunk_width = size // 10
    trunk_height = size // 4
    canvas.create_rectangle(x - trunk_width//2, y - trunk_height, x + trunk_width//2, y, fill='#8B4513')

    for i in range(3):
        canvas.create_polygon(
            x - size//2 + i*size//6, y - trunk_height - i*size//3,
            x + size//2 - i*size//6, y - trunk_height - i*size//3,
            x, y - trunk_height - (i+1)*size//3,
            fill='#228B22', outline='#228B22'
        )

def create_landscape():
    root = tk.Tk()
    root.title("Sunset Landscape")

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    # Sky gradient
    create_gradient(canvas, 0, 0, 800, 300, (255, 100, 0), (0, 0, 100))

    # Sun
    canvas.create_oval(650, 50, 750, 150, fill='#FFD700', outline='#FFD700')

    # Mountains
    for i in range(5):
        x1 = random.randint(-100, 700)
        x2 = x1 + random.randint(200, 400)
        y = random.randint(200, 400)
        color = f'#{random.randint(50, 100):02x}{random.randint(50, 100):02x}{random.randint(50, 100):02x}'
        draw_mountain(canvas, x1, 600, x2, y, color)

    # Ground
    canvas.create_rectangle(0, 450, 800, 600, fill='#228B22', outline='#228B22')

    # Tree
    draw_tree(canvas, 150, 500, 200)

    # Reflection in water
    canvas.create_rectangle(0, 500, 800, 600, fill='', outline='', stipple='gray50')

    root.mainloop()

if __name__ == "__main__":
    create_landscape()
