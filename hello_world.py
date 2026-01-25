import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Hello World")
    window.geometry("300x150")

    label = tk.Label(window, text="Hello, World!", font=("Arial", 24))
    label.pack(expand=True)

    button = tk.Button(window, text="Close", command=window.quit)
    button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
