import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(("127.0.0.1", 9000))
print('服务端启动监听...')
sk.listen()

while True:
    socketObj, clientAddress = sk.accept()
    print(f'{clientAddress}连接成功')
    while True:
        clientMsg = socketObj.recv(1024).strip()
        if len(clientMsg.decode()) > 0:
            print(clientMsg.decode('utf8'))
            socketObj.sendall('Status Code: 200'.encode('utf8'))

        if clientMsg.decode("utf8") == "exit":
            socketObj.sendall("serverexitok".encode('utf8'))
            socketObj.close()
            break

