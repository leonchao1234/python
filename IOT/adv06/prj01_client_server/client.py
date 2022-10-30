import socket

s = socket.socket()
s.connect(("127.0.0.1", 1111))  #連接到伺服器

while True:
    msg = input("Input Message:")  #輸入想要傳送到伺服器的訊息
    s.send(msg.encode("utf8"))  #將訊息編碼後傳送出去
    reply = s.recv(128).decode("utf8")  #接收伺服器回傳的訊息解碼
    if reply == "quit":
        print("disconnected")
        s.close()
        break
    else:
        print(reply)
