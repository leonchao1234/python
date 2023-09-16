######################匯入模組######################
import pygame
import sys
import os


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################

screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption("Snow")
####################撥放音樂######################

####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
####################設定雪花基本參數######################

####################新增fps######################

######################循環偵測######################
paint = False  # 繪圖狀態
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者按關閉鈕
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # 偵測滑鼠按下
            pos = pygame.mouse.get_pos()
            if check_click(pos, 20, 40, 20 + tit_w, 40 + tit_h):
                paint = not (paint)  # 切換繪圖狀態

    if paint:  # 繪圖狀態
        title = font.render("Start", True, (0, 0, 0))
    else:
        title = font.render("Stop", True, (0, 0, 0))

    screen.blit(bg, (0, 0))  # 繪製畫布於視窗左上角
    screen.blit(title, (20, 40))
    pygame.display.update()  # 更新視窗