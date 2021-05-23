from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect(("127.0.0.1", 1212))

initial_data = "#####----- CONNECTED! -----######".encode()
client.sendall(initial_data)
while True:
    dados = client.recv(2048).decode()
    print(f"Data from server >>> {dados}")
    dados = input("[+] Data to the Server >>> ")
    client.sendall(dados.encode())
    if dados =="sair":
        client.close()
        break

