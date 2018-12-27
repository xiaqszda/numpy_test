import socket

ip_port = ("10.33.116.49", 6666)

sk = socket.socket()
sk.connect(ip_port)
# sk.settimeout(5)

while True:
    server_reply = str(sk.recv(1024), encoding="utf-8")
    print(server_reply)
    s = input()
    sk.sendall(bytes(s, encoding='utf-8'))
    if s == "close":
        break
    

sk.close()
