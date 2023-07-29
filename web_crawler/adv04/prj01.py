from ttkbootstrap import *
import sys
import os
from tkinter import filedialog


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    lable.config(text=file_path)


def show_image():  #顯示圖片
    global file_path
    image = Image.open(file_path)  #開啟圖片
    #調大小 antialias是高質量的縮放濾波器
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()),
                         Image.ANTIALIAS)#轉換成tkinter可用的格式
    photo = ImageTk.PhotoImage(image)#顯示圖片 靠左上
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo


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
button = Button(win, text="瀏覽", command=open_file, style="my.TButton")
button.grid(row=0, column=2, stick="W")
button2 = Button(win, text="顯示", command=show_image, style="my.TButton")
button2.grid(row=1, column=0, columnspan=3, sticky="EW")
canvas = Canvas(win, width=400, height=450)
canvas.grid(row=2, columnspan=3)
win.mainloop()
