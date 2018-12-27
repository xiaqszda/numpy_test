import socket

ip_port = ("0.0.0.0", 6666)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)


while True:
    # print("啦啦啦啦啦啦啦啦")
    conn, addr = sk.accept()
    print(conn)
    print(addr)
    s = "连接上了"
    b = bytes(s, encoding='utf-8')
    conn.sendall(b)
    flag = True
    while flag:
        client_data = conn.recv(1024)
        print(str(client_data, encoding='utf-8'))
        if client_data == b"close":
            flag = False
            conn.sendall(b'close')
            conn.close()
            sk.close()
            break
        else:
            conn.sendall(bytes('输入正确的啦啦啦', encoding='utf-8'))
            print('继续运行')
    break
    # conn.close()
