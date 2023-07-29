from ttkbootstrap import *
import sys
import os

os.chdir(sys.path[0])


def test():
    print("test")


font_size = 20
win = tk.Tk()
win.title("My GUI")
win.option_add("*font", ("Helvetica", font_size))

style = Style(theme="vapor")
style.configure("my.TButton", font=("Helvetica", font_size))

lable = Label(win, text="選擇檔案：")
lable.grid(row=0, column=0, sticky="E")
lable = Label(win, text="無")
lable.grid(row=0, column=1, sticky="E")
button = Button(win, text="瀏覽", command=test, style="my.TButton")
button.grid(row=0, column=2, stick="W")
button2 = Button(win, text="顯示", command=test, style="my.TButton")
button2.grid(row=1, column=0, columnspan=3, sticky="EW")
canvas = Canvas(win, width=400, height=450)
canvas.grid(row=2, columnspan=3)
win.mainloop()
