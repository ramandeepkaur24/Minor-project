import tkinter
from tkinter import *
# Import module
from tkinter import *

# Create object
police_root = Tk()

# Adjust size
police_root.geometry("200x200")


# Change the label text
def show():
    if clicked.get() == "Monday":
        mylabel = Label(police_root,text="hi").pack()


global option
# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Monday")

# Create Dropdown menu
drop = OptionMenu(police_root, clicked, *options)
drop.pack()

# Create button, it will change label text
button = Button(police_root, text="click Me", command=show).pack()

# Create Label
label = Label(police_root, text="")
label.pack()

# Execute tkinter
police_root.mainloop()
