import os
import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pytube import YouTube  # pip install -U pytube
from moviepy.editor import *


def call_weather_api(lon: str = "121.5319", lat: str = "25.0478") -> dict:
    """ 使用OpenWeatherMap API獲取天氣資訊 """
    # 使用OpenWeatherMap API獲取天氣資訊
    api_key = "892da2f13edf3c7f382637760e72d224"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"

    exclude = "minutely,hourly"  # 不要分鐘級和小時級的資料
    units = "metric"
    lang = "zh_tw"
    send_url = base_url
    send_url += "lat=" + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_key
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    response = requests.get(send_url)  # 發送請求，獲得天氣資訊
    info = response.json()  # 將json格式轉換為字典
    return info


def get_plot_fig(xlist, ylist, title, xlabel, ylabel) -> plt.Figure:
    """建立圖表"""
    module_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(module_dir, "TaipeiSansTCBeta-Bold.ttf")
    font = FontProperties(fname=font_path, size=14)
    fig, ax = plt.subplots()  # 建立圖表
    ax.plot(xlist, ylist)
    ax.set_title(title, fontproperties=font)
    ax.set_ylabel(ylabel, fontproperties=font)
    ax.set_xlabel(xlabel, fontproperties=font)
    return fig


def save_weather_icon(icon_code):
    """下載並保存天氣圖標"""
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    with open(f"{icon_code}.png", "wb") as icon_file:
        icon_file.write(response.content)


def get_7_Days_weather(info: dict):
    """獲取七天天氣資訊, 回傳日期和溫度的list"""
    dates = []
    temps = []
    for i in range(7):
        temp = info["daily"][i]["temp"]["day"]
        time = datetime.datetime.fromtimestamp(
            info["daily"][i]["dt"]).strftime("%m/%d")
        dates.append(time)
        temps.append(temp)
        print(f"{time} 的溫度是 {temp} 度")
    return dates, temps


def get_video_info(url: str):
    yt = YouTube(url)
    title = yt.title
    author = yt.author
    length = yt.length
    image_url = yt.thumbnail_url

    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    res = []
    for stream in streams:
        res.append(stream.resolution)
    return title, author, length, image_url, res


########################主程式##############################
def download_video(url: str, r: str, on_progress_callback=None):
    yt = YouTube(url, on_progress_callback=on_progress_callback)
    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    res = []
    for stream in streams:
        res.append(stream.resolution)

    if r in res:
        stream = streams.filter(res=r)[0]
        stream.download()
        return True
    else:
        return False


#######################切割影片########################
def cut_video(video_path: str, beg: int, end: int):
    """切割影片 video_path: 影片檔案路 beg: 開始時間(秒) end: 結束時間(秒)"""
    if end <= beg:
        print("結束時間必須大於開始時間")
        return False
    if os.path.isfile(video_path):  # 判斷影片檔案是否存在
        clip = VideoFileClip(video_path)  # 讀取影片檔案
        length = clip.duration  # 影片長度
        print(f"影片長度:{length}秒")
        clip = clip.subclip(beg, end)  # 切割影片
        title = video_path.split(".")[0]  # 影片檔案名稱
        new_file_name = f"{title}-{beg}-{end}.mp4"
        clip.write_videofile(new_file_name)  # 儲存影片
        print(f"影片儲存於{new_file_name}")
        return True
    else:
        print("找不到影片檔案")
        return False


#######################合併影片########################
def merge_video(file_name_list: list, output_file_name: str):
    """合併影片, file_name_list: 要合併的影片檔案名稱清單, output_file_name: 輸出的檔案名稱"""
    for file_name in file_name_list:
        if not os.path.exists(file_name):
            print(f"錯誤: {file_name}不存在")
            return False

    video_list = []
    for file_name in file_name_list:
        video_list.append(VideoFileClip(file_name))
    final_clip = concatenate_videoclips(video_list)
    final_clip.write_videofile(output_file_name)
    return True


#######################影片轉GIF########################
def video_to_gif(video_path: str, gif_path: str) -> bool:
    if os.path.isfile(video_path):
        clip = VideoFileClip(video_path)
        clip.write_gif(gif_path)
        return True
    else:
        return False