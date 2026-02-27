import tkinter as tk
import math


def open_triangle_window(parent):
    win = tk.Toplevel(parent)
    win.title("Spinning Triangle")
    win.geometry("300x300")

    canvas = tk.Canvas(win, width=300, height=300, bg="white")
    canvas.pack()

    angle = [0]
    cx, cy, r = 150, 150, 100

    def draw_triangle():
        canvas.delete("triangle")
        points = []
        for i in range(3):
            a = math.radians(angle[0] + i * 120)
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            points.extend([x, y])
        canvas.create_polygon(points, fill="red", outline="darkred", width=2, tags="triangle")
        angle[0] = (angle[0] + 2) % 360
        win.after(16, draw_triangle)

    draw_triangle()


def main():
    window = tk.Tk()
    window.title("Hello World")
    window.geometry("300x150")

    label = tk.Label(window, text="Hello, World!", font=("Arial", 24))
    label.pack(expand=True)

    button = tk.Button(window, text="Open Triangle", command=lambda: open_triangle_window(window))
    button.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()
