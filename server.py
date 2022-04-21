import socket
import helper as help

_host = "127.0.0.1"
_port = 8000

p, q, e, d = 47, 71, 97, 1693
n = p * q

client_e = 0
client_n = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(15)
    s.bind((_host, _port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by {}".format(addr))
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                break
            if data.decode() == "REGISTER":
                print("hello")
                conn.sendall(("keys,{},{}".format(e, n)).encode())
                data = conn.recv(1024)
                client_e, client_n = data.decode().split(',')
                print(client_e)
                print(client_n)

