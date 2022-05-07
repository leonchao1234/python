# x = input("please input number:")
# i = 0
# while i < x:
#     Value = "*" + 2 * i * "*"
#     print(Value.center(x * 2 - 1))
#     i += 1
# j = 0
# while j < x:
#     Value = "*"
#     print(Value.center(x * 2 - 1))
#     j += 1
import turtle

turtle.pensize(5)
turtle.stamp()
turtle.begin_fill()
for i in range(8):
    turtle.forward(100)
    turtle.stamp()
    turtle.right(50)
    turtle.stamp()
turtle.done()