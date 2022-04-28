import socket
import hashlib
import helper as help

_host = "127.0.0.1"
_port = 8000

p, q, e, d = 47, 71, 97, 1693
n = p * q

client_e, client_n = 0, 0

clients = {}

logged_in = help.Client(["","","","","",""])

# _port = int(input("input a port number "))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(15)
    s.bind((_host, _port))
    s.listen()
    conn, addr = s.accept()
    data = conn.recv(1024)
    keys = (data.decode()).split(',')
    client_e, client_n = (int)(keys[0]), (int)(keys[1])
    conn.sendall(("{},{}".format(e, n)).encode())
    h = hashlib.new('sha256')
    with conn:
        print("Connected by {}".format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            elif data.decode() == "REGISTER":
                conn.sendall("ENTRY".encode())
                data = conn.recv(1024)
                user_data = []
                for i in ["Last Name", "First Name", "Major", "Hometown", "Username"]:
                    conn.sendall("Input your {}".format(i).encode())
                    data = conn.recv(1024)
                    user_data.append(help.rsa_encryption(data.decode(), d, n))
                conn.sendall("Input your password".encode())
                
                data = conn.recv(1024)
                user_data.append(hash(user_data[-1] + help.rsa_encryption(data.decode(), d, n)))
                user = help.Client(user_data)
                print(user.toJSON())
                clients[user.username] = user
                conn.sendall("COMPLETE".encode())

                

            elif data.decode() == "LOGIN":
                conn.sendall(b"ENTRY")
                conn.recv(1024)
                conn.sendall(b"enter Username")
                data = conn.recv(1024)
                uname = help.rsa_encryption(data.decode(), d, n)
                conn.sendall(b"enter Password")
                data = conn.recv(1024)
                pswd = help.rsa_encryption(data.decode(), d, n)
                try:
                    h.update((uname + pswd).encode())
                    if clients[uname].password == hash(uname+pswd):
                        logged_in = clients[uname]
                        conn.sendall(b"Connected\nEnter 'y' to continue...")
                    else:
                        conn.sendall(b"Invalid Username or Password\nEnter 'y' to continue...")
                except:
                    conn.sendall(b"Invalid Username or Password\nEnter 'y' to continue EXCEPTION...")
                data = conn.recv(1024)
                conn.sendall("COMPLETE".encode())

            elif data.decode() == "VIEW_REGISTRATION":
                if logged_in.username == "":
                    conn.sendall(b"ERROR")
                    conn.recv(1024)
                    continue
                conn.sendall(b"SENDING JSON")
                data = conn.recv(1024)
                conn.sendall(help.rsa_encryption(logged_in.toJSON(), client_e, client_n).encode())

            else:
                conn.sendall("Invalid Message".encode())

            

