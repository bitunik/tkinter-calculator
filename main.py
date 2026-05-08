import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar()

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief="sunken"
        )
        display.pack(fill="both", padx=10, pady=10, ipady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ("C", 0, 0), ("←", 0, 1), ("%", 0, 2), ("÷", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("×", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2),
        ]

        for text, row, col in buttons:
            if text == "0":
                btn = tk.Button(
                    button_frame, text=text, font=("Arial", 18),
                    command=lambda t=text: self.click(t)
                )
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
            elif text == "=":
                btn = tk.Button(
                    button_frame, text=text, font=("Arial", 18),
                    command=self.evaluate, bg="#4CAF50", fg="white"
                )
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
            else:
                btn = tk.Button(
                    button_frame, text=text, font=("Arial", 18),
                    command=lambda t=text: self.click(t)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

    def bind_keys(self):
        self.root.bind("<Key>", self.on_keypress)
        self.root.bind("<Return>", lambda event: self.evaluate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())

    def click(self, key):
        if key == "C":
            self.clear()
        elif key == "←":
            self.backspace()
        elif key == "=":
            self.evaluate()
        elif key == "×":
            self.expression += "*"
            self.display_var.set(self.expression.replace("*", "×").replace("/", "÷"))
        elif key == "÷":
            self.expression += "/"
            self.display_var.set(self.expression.replace("*", "×").replace("/", "÷"))
        elif key == "%":
            self.expression += "/100"
            self.display_var.set(self.expression.replace("*", "×").replace("/", "÷"))
        else:
            self.expression += str(key)
            self.display_var.set(self.expression.replace("*", "×").replace("/", "÷"))

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression.replace("*", "×").replace("/", "÷"))

    def evaluate(self):
        try:
            result = eval(self.expression)
            self.display_var.set(str(result))
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Error", "Invalid expression")
            self.clear()

    def on_keypress(self, event):
        key = event.char
        allowed = "0123456789+-*/.%()"

        if key in allowed:
            self.click(key)
        elif key == "\r":
            self.evaluate()
        elif event.keysym == "BackSpace":
            self.backspace()
        elif event.keysym == "Escape":
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
