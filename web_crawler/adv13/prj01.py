from ttkbootstrap import *
import time
import sys
import os
from myfunction.myfunction import *


def start_progress():
    for i in range(101):
        progress["value"] = i
        percent_label.config(text=f"{i}%")
        win.update()
        time.sleep(0.05)


def get_video_info_gui():
    _, _, _, _, res = get_video_info(entry.get(), show_progress)
    res_option['menu'].delete(0, 'end')
    for r in res:
        res_option["menu"].add_command(lable=r, command=tk.setit(res_var))
    res_var.set(res[0])


def download_video_gui():
    if download_video(entry.get(), res_var.get()):
        lable3.config(text="下載完成")
    else:
        lable3.config(text="解析度錯誤")


def show_progress(stream, chunk, bytes_remaining):
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    percent_label.config(text=f"{percent:.2f}%")
    progress["value"] = percent
    win.update()


win = tk.Tk()
win.title("Progress Bar Example")

font_size = 20

lable = Label(win, text="請輸入Youtube影片網址:")
lable.grid(row=0, column=0, sticky="E")
entry = Entry(win, width=30)
entry.grid(row=0, column=1, sticky="E")
button = Button(win,
                text="搜尋影片資訊",
                command=get_video_info_gui,
                style="my.TButton")
button.grid(row=0, column=2, stick="W")
lable2 = Label(win, text="請選擇影片解析度")
lable2.grid(row=1, column=0, columnspan=1, sticky="EW")
button2 = Button(win,
                 text="下載影片",
                 command=download_video_gui,
                 style="my.TButton")
button2.grid(row=1, column=2, stick="W")
lable3 = Label(win, text="下載完成")
lable3.grid(row=2, column=0, columnspan=1, sticky="EW")
res_var = tk.StringVar()
res_option = OptionMenu(win, res_var, ())
res_option.grid(row=1, column=1, padx=10, pady=10)

progress = Progressbar(win, orient=HORIZONTAL, length=200, mode="determinate")
progress.grid(row=2, column=1, padx=10, pady=10)

percent_label = Label(win, text="")
percent_label.grid(row=2, column=2, padx=10, pady=10)
win.mainloop()