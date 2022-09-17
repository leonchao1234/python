-*- coding:utf-8 -*-
def add_juice(a_list):
    y = input("請輸入想加入果汁")
    if not (y in a):
        a.append(y)
    return a_list

def show_juice(a_list):
    print(a_list)

def remove_juice(a_list):
    y = input("請輸入想刪除的果汁：")
    if y in a_list:
        a_list.remove(y)
    return a_list

a = []
op = [add_juice, add_juice, show_juice, remove_juice]
while True:
    x = int(input("1.想加入菜單的果汁 \n 2.顯示出目前所有果汁 \n3.刪除特定果汁 \n4.離開系統"))
    if x == len(op) + 1:
        print("掰掰")
        break
#     a = op[x - 1](a)
# import turtle

# def tree_leaves(x, y):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.setheading(0)
#     turtle.color("yellow")
#     turtle.begin_fill()
#     turtle.forward(90)
#     turtle.left(120)
#     turtle.forward(90)
#     turtle.left(120)
#     turtle.forward(90)
#     turtle.end_fill()

# def treee_trunk(x, y):
#     turtle.penup()
#     turtle.goto(x + 12.5, y)
#     turtle.pendown()
#     turtle.setheading(0)
#     turtle.color("brown")
#     turtle.begin_fill()
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.end_fill()

# tree_leaves(0, 0)
# tree_leaves(20, 0)
# tree_leaves(40, 0)
# treee_trunk(30, 0)

# turtle.done()

import random
import turtle

i = ["green", "blue", "red"]


def tree_leaves(x, y):
    r = float(random.randint(0, 100)) / 100
    g = float(random.randint(0, 100)) / 100
    b = float(random.randint(0, 100)) / 100
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(r, g, b)
    turtle.begin_fill()
    turtle.forward(90)
    turtle.left(120)
    turtle.forward(90)
    turtle.left(120)
    turtle.forward(90)
    turtle.end_fill()


def treee_trunk(x, y):
    r = float(random.randint(0, 100)) / 100
    g = float(random.randint(0, 100)) / 100
    b = float(random.randint(0, 100)) / 100
    # print(r, g, b)
    turtle.penup()
    turtle.goto(x + 12.5, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(r, g, b)
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()


import random

turtle.speed(0)
for i in range(10):
    pos_x = random.randint(-200, 100)
    pos_y = random.randint(-200, 200)
    tree_leaves(pos_x + 10, pos_y)
    tree_leaves(pos_x + 40, pos_y)
    tree_leaves(pos_x + 70, pos_y)
    treee_trunk(pos_x + 50, pos_y)

turtle.done()