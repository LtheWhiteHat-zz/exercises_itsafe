from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Client >>> ")
    client.sendto(data.encode(),("127.0.0.1", 3333))
    data, server = client.recvfrom(2048)
    clear_data = data.decode()
    print(clear_data)
