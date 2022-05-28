# -*- coding:utf-8 -*-
# min = input("please input the minimum number of the range:")
# max = input("please input the maximum number of the range:")
# mul = input("please input the number that you want to skip:")
# for i in range(min, max):
#     if i % mul == 0:
#         continue
# #     print(i)
# ans = input("input a sentence:")
# print(ans.split("p"))
# print(list("fkksvvds"))
# print(list("1234"))
# print(list("True"))
# print(list("2.56"))
# i = ['a', 'b', 'c']
# print(i[0])
# i = ['a', 'b', 'c']
# print(i[0])
# i[2] = 'a'
# print(i)
# i = ["a,b,c"]
# i.append("d")
# print(i)
# i = ["a", "b", "c"]
# i.remove("b")
# print(i)
# i = [1, 2, 3]
# i.insert(0, "0")
# print(i)
# i = [1, 2, 3]
# i.pop(1)
# print(i)
# i = [5, 2, 3, 8, 100]
# i.sort()
# print(i)
# i = ["b", "a", "c"]
# i.sort()
# print(i)
# i = [1, 2, 3]
# i.reverse()
# print(i)
# from operator import index

# i = ['a','b','c']
# index =1.index ('a')
# print(index)
#  input("1.想加入菜單的果汁 2.顯示出目前所有果汁 3.離開系統")
def add_juice(a_list):
    a_list=[]

def show_juice(a_list):


a=[]
while True:
    x=input("1.想加入菜單的果汁 \n 2.顯示出目前所有果汁 \n3.離開系統")
    if x==1:
       a=add_juice(a)
        # y=input("請輸入想加入果汁")
        # if not (y in a):
        #     a.append(y)
        elif x==2:
            print(a)
        else:
            print("掰掰")
            break
        

