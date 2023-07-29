from moviepy.editor import *
import sys
import os
from myfunction.myfunction import *

os.chdir(sys.path[0])
u = "https://www.youtube.com/watch?v=WlfIYn8-1pI"
title, length, _, _, res = get_video_info(u)
print(res)

r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")
if download_video(u, r):
    print("下載完成")
else:
    print("找不到該解析度的影片")

video_path = f"{title}.mp4"
if os.path.isfile(video_path):
    clip = VideoFileClip(video_path)
    print(f"影片長度:{length}秒")
    beg = int(input("請輸入要切割的開始時間（秒）："))
    end = int(input("請輸入要切割的結束時間（秒）："))
    clip = clip.subclip(beg, end)
    new_file_name = f"{title}-{beg}-{end}.mp4"
    clip.write_videofile(new_file_name)
    print(f"影片儲存於{new_file_name}")
else:
    print("找不到影片檔案")

#######################切割影片########################
beg = int(input("請輸入要切割的開始時間（秒）："))
end = int(input("請輸入要切割的結束時間（秒）："))
result = "剪輯完成" if cut_video(f"(title.mp4", beg, end) else "剪輯失敗"
print(result)