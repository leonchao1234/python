from tkinter import *
import random as r

win = Tk()
win.title("My first GUI")

clear = False

color = [
    "black",
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "lime",
    "maroon",
    "navy",
    "olive",
    "teal",
    "violet",
    "indigo",
    "coral",
    "crimson",
    "hotpink",
    "khaki",
    "lavender",
    "lavenderblush",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightsteelblue",
    "lightyellow",
]


def hi_fun():
    global clear
    display.config(text="Hi Singular", fg=color[r.randint(0, len(color) - 1)])
    # print("Hello Singular")
    # if clear == True:
    #     display.config(text="", fg="white", bg="white")
    # else:
    #     display.config(text="Hi Singular", fg="red", bg="black")
    # clear = not (clear)


btn = Button(win, text="Click me", command=hi_fun)
btn.pack()
display = Label(win, text="hi", fg="red", bg="black")
display.pack()
win.mainloop()
