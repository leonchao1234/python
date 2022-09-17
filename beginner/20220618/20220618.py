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
    t = 2  #attack speed
    monster_life = random.randint(2, 10)
    print("Monster Life = {}".format(monster_life))
    while True:
        attack = random.randint(1, 3)
        print("You make damage %d" % attack)
        monster_life -= attack
        time.sleep(t)
        print("Monster Life %d" % monster_life)

        if (monster_life < 1):
            print("You beat monster")
            s[2] += random.randint(10, 20)
            break
        else:
            print("Monster Attack")
            s[1] -= 100
            time.sleep(t)
            print("you hurt,Life=%d" % s[1])
            if (s[1] < 1):
                print("you dead")
                s[0] = 0
                break


file = "save.txt"
status = []
try:
    f = open(file, "r")
except:
    status = [1, 10, 50]
else:
    for line in f:
        status.append(int(line))
    f.close()

print("目前角色狀態:HP={},Money={}".format(status[1], status[2]))
event = [update_life, update_money, fighting]

while True:
    ans = input("continue(1/2)?:")
    if ans == "1":
        event[random.randrange(0, len(event))](status)
        print("目前角色狀態:HP={},Money={}".format(status[1], status[2]))
        if status[0] == 0:
            print("game over")
            if status[2] >= 50:
                ans = input("是否購買生命藥水?:")
                if ans == "y":
                    status[0] = 1
                    status[1] = 10
                    status[2] -= 50
                    for i in range(10):
                        print(">" * i, end="\r")
                        time.sleep(0.5)
                    print("\n!!恭喜復活!!")
                else:
                    break
    else:
        print("881")
        file = "save.txt"
        f = open(file, "w")
        for i in status:
            f.write(str(i) + '\n')
        f.close()
        break
