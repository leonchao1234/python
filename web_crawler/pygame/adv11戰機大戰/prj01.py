import pygame
import sys
import os
from pygame.locals import *

os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()
#載入圖片
img_sship = pygame.image.load("fighter_M.png")
img_bg = pygame.image.load("space.png")
#遊戲視窗設定
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
roll_y = 0
#玩家設定
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship.get_width() / 2
ss_hh = img_sship.get_height() / 2


#定義函式
def roll_bg():
    """更新背景"""
    global roll_y

    roll_y = (roll_y + 20) % bg_y  # 背景移動
    screen.blit(img_bg, (0, roll_y - bg_y))  # 背景圖左移
    screen.blit(img_bg, (0, roll_y))  # 背景圖接續顯示


#主程式
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F1:
                screen = pygame.display.set_mode(bg_size)
    roll_bg()
    pygame.display.update()