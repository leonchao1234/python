from ttkbootstrap import *
import sys
import os
from tkinter import filedialog

font_size = 20
win = tk.Tk()
win.title("My GUI")
win.option_add("*font", ("Helvetica", font_size))

style = Style(theme="vapor")
style.configure("my.TButton", font=("Helvetica", font_size))

entry = Entry(win, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


def show_result():
    entry_text = entry.get()

    try:
        ans = eval(entry_text)
        lable.config(text=ans)
    except:
        lable.config(text="error")


button = Button(win, text="顯示計算結果", command=show_result, style="my.TButton")
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
lable = Label(win, text="計算結果：")
lable.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

win.mainloop()