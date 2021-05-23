from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(("", 3333))
print("Waiting for connections!")

while True:
    data, client = server.recvfrom(2048)
    clear_data = data.decode()
    print(clear_data)
    if clear_data == "exit":
        server.close()
        break
    data = input("Server >>> ")
    server.sendto(data.encode(), client)
