import socket
import telnetlib

def scan_port(ip, port):
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.settimeout(1000)
    sock = telnetlib.Telnet()
    try:
        # sock.connect((ip, port))
        sock.open(ip, port)
        print("port", port, " is open.")
    except Exception:
        # print("port", port, " is closed.")
        # print(e)
        pass
    sock.close()


if __name__ == '__main__':
    ip = "10.33.116.20"
    Sport = 1
    Eport = 300

    for port in range(Sport, Eport):
        scan_port(ip, port)

