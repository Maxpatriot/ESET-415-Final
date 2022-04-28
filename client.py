import socket
import helper as help

_host = "127.0.0.1"
_port = 8001

p, q, e, d = 83, 61, 53, 557
n = p * q

server_e = 0
server_n = 0

_port = int(input("input a port number "))

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
    print("Connected to {}::{}".format(_host, _port))
    
    # exchange keys with server
    s.sendall("{},{}".format(e, n).encode())
    data = s.recv(1024)
    keys = (data.decode()).split(',')
    server_e, server_n = (int)(keys[0]), (int)(keys[1])
    help.printMenu()
    while data.decode() != "QUIT":
        message = input("-> ")
        s.sendall(message.encode())
        data = s.recv(1024)
        # print(data.decode())
        if not data:
            break
 

        if data.decode() == "ENTRY":
            s.sendall("In entry mode".encode())
            data = s.recv(1024)
            while data.decode() != "COMPLETE":
                print(data.decode())
                message = input("-> ")
                s.sendall(help.rsa_encryption(message, server_e, server_n).encode())
                data = s.recv(1024)
            help.printMenu()

        if data.decode() == "SENDING JSON":
           s.sendall(b"ready to recieve")
           data = s.recv(1024)
           print(help.rsa_encryption(data.decode(), d, n))

        if data.decode() == "ERROR":
            print("Invalid message sent")
            s.sendall(b"ready to send")
        
