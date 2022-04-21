import socket
import helper as help

_host = "127.0.0.1"
_port = 8000

p, q, e, d = 83, 61, 53, 557
n = p * q

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(10)
    try:
        s.connect((_host, _port))
    except socket.error as msg:
        print ("Socket Error: %s" % msg)
        exit()
    except TypeError as msg:
        print ("Type Error: %s" % msg)
        exit()
    print("Connected to server...")
    message = input("Input a message to send\n-> ")
    s.sendall(message.encode())
    data = s.recv(1024)
    while data.decode() != "EXIT":
        print("Received {}".format(data.decode()))
        s.sendall("{},{}".format(e, n).encode())
