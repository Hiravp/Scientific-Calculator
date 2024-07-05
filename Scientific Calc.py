import math
import tkinter as tk
from tkinter import messagebox

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("480x600")
        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display frame
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field

        # Buttons frame
        buttons_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        buttons_frame.pack()

        # First row
        self.create_button(buttons_frame, "7", 1, 0)
        self.create_button(buttons_frame, "8", 1, 1)
        self.create_button(buttons_frame, "9", 1, 2)
        self.create_button(buttons_frame, "/", 1, 3)

        # Second row
        self.create_button(buttons_frame, "4", 2, 0)
        self.create_button(buttons_frame, "5", 2, 1)
        self.create_button(buttons_frame, "6", 2, 2)
        self.create_button(buttons_frame, "*", 2, 3)

        # Third row
        self.create_button(buttons_frame, "1", 3, 0)
        self.create_button(buttons_frame, "2", 3, 1)
        self.create_button(buttons_frame, "3", 3, 2)
        self.create_button(buttons_frame, "-", 3, 3)

        # Fourth row
        self.create_button(buttons_frame, "0", 4, 0)
        self.create_button(buttons_frame, ".", 4, 1)
        self.create_button(buttons_frame, "+", 4, 2)
        self.create_button(buttons_frame, "=", 4, 3, self.equal_button)

        # Fifth row
        self.create_button(buttons_frame, "C", 5, 0, self.clear_button)
        self.create_button(buttons_frame, "sin", 5, 1, lambda: self.append_function("sin("))
        self.create_button(buttons_frame, "cos", 5, 2, lambda: self.append_function("cos("))
        self.create_button(buttons_frame, "tan", 5, 3, lambda: self.append_function("tan("))

        # Sixth row
        self.create_button(buttons_frame, "log", 6, 0, lambda: self.append_function("log10("))
        self.create_button(buttons_frame, "sqrt", 6, 1, lambda: self.append_function("sqrt("))
        self.create_button(buttons_frame, "(", 6, 2)
        self.create_button(buttons_frame, ")", 6, 3)

    def create_button(self, frame, text, row, col, command=None):
        if command is None:
            command = lambda: self.button_click(text)
        button = tk.Button(frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=command)
        button.grid(row=row, column=col, padx=1, pady=1)

    def button_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear_button(self):
        self.expression = ""
        self.input_text.set("")

    def append_function(self, func):
        self.expression += func
        self.input_text.set(self.expression)

    def equal_button(self):
        try:
            # Evaluate the expression safely
            result = self.evaluate_expression(self.expression)
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""

    def evaluate_expression(self, expression):
        # Safely evaluate the mathematical expression
        # Support functions: sin, cos, tan, log10, sqrt, radians, etc.
        allowed_names = {"sin": math.sin, "cos": math.cos, "tan": math.tan,
                         "log10": math.log10, "sqrt": math.sqrt, "radians": math.radians}

        code = compile(expression, "<string>", "eval")

        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Use of {name} is not allowed")

        return eval(code, {"__builtins__": {}}, allowed_names)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
