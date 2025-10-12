from tkinter import *

# Create main window
root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field for input/output
entry = Entry(root, width=25, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to insert numbers/operators
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

# Function to clear the entry
def button_clear():
    entry.delete(0, END)

# Function to calculate result
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, width=5, height=2, bg="lightgreen", command=button_equal).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
Button(root, text="Clear", width=22, height=2, bg="lightcoral", command=button_clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run GUI loop
root.mainloop()
