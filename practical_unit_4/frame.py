from tkinter import *
# create root window
root = Tk()
# give a title for root window
root.title("My Frame")
# crete a frame as child to root window
f = Frame(root, height=400, width="500", bg="light blue", cursor="cross")
# attach the frame to root window
f.pack()
# let the root window wait for any events
root.mainloop()