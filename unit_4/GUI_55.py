from tkinter import *

# Create main window
root = Tk()
root.title("Simple GUI Example")
root.geometry("300x200")

# Define a function for button click
def display_text():
    user_text = entry.get()
    label_result.config(text="Hello, " + user_text + "!")

# Create a label
label = Label(root, text="Enter your name:")
label.pack(pady=5)

# Create an entry field
entry = Entry(root, width=25)
entry.pack(pady=5)

# Create a button
button = Button(root, text="Submit", command=display_text)
button.pack(pady=10)

# Create a label to display the result
label_result = Label(root, text="")
label_result.pack(pady=5)

# Run the GUI loop
root.mainloop()
