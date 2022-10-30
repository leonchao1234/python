import socket  #導入模組

HOST = "localhost"  #IP
PORT = 1111  #伺服器的號碼
s = socket.socket()  # create server
s.bind((HOST, PORT))  # server setting IP port
s.listen(5)  #伺服器端最多可接受多少socket
print("server:{} port:{} start".format(HOST, PORT))
client, addr = s.accept()  #伺服器端接收並會回傳對象與IP位址資訊
print("client address:{},port:{}".format(addr[0], addr[1]))

while True:
    msg = client.recv(100).decode("utf8")  #接收客戶端訊息
    print("Recieve Message:" + msg)
    reply = ""  #建立伺服器回應字串
    if msg == "Hi":
        client.send(b"Hello!")
    elif msg == "bye":
        client.send(b"quit")
        break
    else:
        client.send(b"what??")

client.close()  #關閉與客戶端溝通
s.close()  #關密伺服器
