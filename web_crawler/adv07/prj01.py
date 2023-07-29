import requests
import os
from tkinter import *
from ttkbootstrap import *
import sys

os.chdir(sys.path[0])
api_key = "b4ccba82e413dab0d5670f051a0f09c1"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
units = "metric"
lang = "zh_tw"


def get_weather_info():
    city_name = city_name_entry.get()
    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    response = requests.get(send_url)
    info = response.json()

    print(info)
    print(f'city = {info["name"]}')
    print(f'temp = {info["main"]["temp"]}')
    print(f'description = {info["weather"][0]["description"]}')

    if "main" in info.keys():
        global current_temperature
        temp_info = info["main"]
        current_temperature = temp_info["temp"]
        weather_info = info["weather"][0]
        weather_description = weather_info["description"]
        icon_code = weather_info['icon']
        icon_code = info["weather"][0]["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f"{icon_code}.png", "wb") as icon_file:
            icon_file.write(response.content)

        image = Image.open(f"{icon_code}.png")
        tk_image = ImageTk.PhotoImage(image)
        lable2.config(image=tk_image)
        lable2.image = tk_image

        lable3.config(text=f'溫度:{current_temperature}C')
        lable4.config(text=f'描述:{weather_description}')
    else:
        print("City Not Found")


font_size = 20
win = tk.Tk()
win.title("My GUI")
win.option_add("*font", ("Helvetica", font_size))

style = Style(theme="vapor")
style.configure("my.TButton", font=("Helvetica", font_size))

lable1 = Label(win, text="請輸入想搜尋的城市：")
lable1.grid(row=0, column=0, sticky="E")
lable2 = Label(win, text="天氣圖標：")
lable2.grid(row=1, column=0, sticky="W")
lable3 = Label(win, text="溫度:?C")
lable3.grid(row=1, column=1, sticky="W")
lable4 = Label(win, text="描述？")
lable4.grid(row=1, column=2, sticky="W")
button = Button(win,
                text="獲得天氣資訊",
                style="my.TButton",
                command=get_weather_info)
button.grid(row=0, column=2, stick="W")

city_name_entry = Entry(win)
city_name_entry.grid(row=0, column=1)


def on_switch_change():
    global units, current_temperature
    if check_type.get():
        units = "metric"
    else:
        units = "imperial"

    if lable3.cget("text") != "溫度:?C":
        if units == "metric":
            current_temperature = round((current_temperature - 32) * 5 / 9, 2)
            lable3.config(text=f"溫度:{current_temperature}C")
        elif units == "imperial":
            current_temperature = round(current_temperature * 9 / 5 + 32, 2)
            lable3.config(text=f"溫度:{current_temperature}F")


style = Style(theme="vapor")
style.configure("my.TButton", font=("Helvetica", font_size))
check_type = BooleanVar()
check_type.set(True)

check = Checkbutton(win,
                    text="溫度單位(C/F)",
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)
check.grid(row=3, column=1)

win.mainloop()
