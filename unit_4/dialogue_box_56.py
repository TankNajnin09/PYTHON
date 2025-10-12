from tkinter import *
from tkinter import messagebox

# Create main window
root = Tk()
root.title("Dialog Example")
root.geometry("300x200")

# Function to show an information alert
def show_alert():
    messagebox.showinfo("Information", "This is an alert message!")

# Function to ask confirmation
def ask_confirmation():
    answer = messagebox.askyesno("Confirmation", "Do you want to continue?")
    if answer:
        messagebox.showinfo("Result", "You selected YES")
    else:
        messagebox.showwarning("Result", "You selected NO")

# Create Buttons
btn_alert = Button(root, text="Show Alert", command=show_alert)
btn_alert.pack(pady=10)

btn_confirm = Button(root, text="Ask Confirmation", command=ask_confirmation)
btn_confirm.pack(pady=10)

# Run the GUI loop
root.mainloop()
