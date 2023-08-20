import socket

clientSk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSk.connect(("127.0.0.1", 9000))
while True:
    msg = input("请输入信息>>:").strip()
    if len(msg) == 0:
        continue

    clientSk.sendall(msg.encode('utf8'))

    ret = clientSk.recv(1024)
    if ret:
        print(ret.decode("utf8"))
        if ret.decode("utf8") == "serverexitok":
            break
