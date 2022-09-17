# -*- coding:utf-8 -*-
# 初始血量：10點
# 初始錢：0元
# 冒險者攻擊力：1~3
# 怪物攻擊力：1點

# 獲得紅藥水：1~3點血量
# 獲得錢袋：10~30元
#
# 擊敗怪物獲得10~20元
# 回合制 冒險者先攻
# 冒險者隨機對怪物產生1~3點傷害
# 怪物生命隨機2~10點 攻擊力1點
# 戰鬥結束後 更新冒險者狀態

#  status[0]=1活著 0死亡
# status[1]=剩餘生命
# status[2]=剩餘金幣

import random
import time


def update_life(s):
    HP = random.randint(1, 3)
    print("角色獲得{}點HP".format(HP))
    s[1] += HP


def update_money(s):
    Money = random.randint(10, 30)
    print("角色獲得{}元".format(Money))
    s[2] += Money


def fighting(s):
    monsterlife = random.randint(2, 10)
    monsterattack = 1
    peopleattack = random.randint(1, 3)
    print("角色攻擊{}".format(peopleattack))
    print("怪物攻擊{}".format(monsterattack))
    print("怪物生命{}".format(monsterlife))
    x = monsterlife - peopleattack
    print(x)
    y = update_life - monsterattack
    print(y)


status = [1, 10, 0]
event = [update_life, update_money, fighting]

while True:
    ans = input("continue(1/2)?:")
    if ans == 1:
        event[random.randrange(0, len(event))](status)
        print("目前角色狀態:HP={},Money={}".format(status[1], status[2]))
    else:
        print("881")
        break
