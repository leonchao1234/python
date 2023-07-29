from ttkbootstrap import *

import os
import sys

os.chdir(sys.path[0])


def on_switch_change():
    check_label.config(text=str(check_type.get()))


font_size = 20
win = tk.Tk()
win.title("My GUI")
win.option_add("*font", ("Helvetica", font_size))

style = Style(theme="vapor")
style.configure("my.TButton", font=("Helvetica", font_size))
check_type = BooleanVar()
check_type.set(True)
check_label = Label(win, text="True")
check_label.grid(row=1, column=2)
check = Checkbutton(win,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)
check.grid(row=1, column=1)
win.mainloop()
