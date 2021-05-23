import threading
from socket import *


def serve(port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    client, addr = server.accept()
    print(f"Connected from {addr}")
    while True:
        for i in range(10):
            t = threading.Thread(target=client.recv, args=(2048,))
            t.start()
            dados = client.recv(2048).decode()
            print(f"Incoming >>> {dados}")
            output = input("Message >>>")
            client.sendall(output.encode())
            if output == "au revoir":
                client.close
                break

    server.close()


if __name__ == "__main__":
    serve(3232)