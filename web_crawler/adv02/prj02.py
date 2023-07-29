from tkinter import *
import sys
import os

os.chdir(sys.path[0])

win = Tk()
win.title("My first GUI")


def exit_fun():
    win.destroy()


def move_object(event, object, dx, dy):
    canvas.move(object, dx, dy)


quit_btn = Button(win, command=exit_fun)
quit_btn.pack()

canvas = Canvas(win, width=400, height=600)
canvas.pack()
# loading picture
# win.iconbitmap("")
# show picture

img = PhotoImage(file="crocodile2.gif")
circle = canvas.create_oval(100, 100, 300, 300, fill="red")
my_img = canvas.create_image(300, 300, image=img)
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
msg = canvas.create_text(300,
                         100,
                         text="croc",
                         fill="black",
                         font=('Arial', 30))

canvas.bind_all('<Right>', lambda event: move_object(event, circle, 10, 0))
canvas.bind_all('<Left>', lambda event: move_object(event, circle, -10, 0))
canvas.bind_all('<Up>', lambda event: move_object(event, circle, 0, -10))
canvas.bind_all('<Down>', lambda event: move_object(event, circle, 0, 10))
canvas.bind_all('<d>', lambda event: move_object(event, rect, 10, 0))
canvas.bind_all('<a>', lambda event: move_object(event, rect, -10, 0))
canvas.bind_all('<w>', lambda event: move_object(event, rect, 0, -10))
canvas.bind_all('<s>', lambda event: move_object(event, rect, 0, 10))

win.mainloop()
