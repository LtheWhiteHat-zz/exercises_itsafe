import re
import os
import threading

def imprime_numeros(limite):
    for i in range(100000):
        print(i)

threads = []
def executa_threaded():
    ts = []
    for i in range(5):
        thread = threading.Thread(target=imprime_numeros, args=(100000,))
        ts.append(thread)
    #t = threading.Thread(target=imprime_numeros, args=(100000,))
    for t in ts:
        t.start()
    for thread in ts:
        thread.join()



def mult(num1, num2):
    return num1*num2

def division(num1, num2):
    return num1/num2

def sum(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def calc(**kwargs):
    if kwargs is not None:
        num1 = kwargs["num1"]
        num2 = kwargs['num2']
        if "operation" in kwargs.keys():
            if kwargs["operation"] == "soma":
                return str(sum(num1,num2))
            elif kwargs["operation"] == "sub":
                return str(sub(num1, num2))
            elif kwargs["operation"] == "mult":
                return str(mult(num1, num2))
            elif kwargs["operation"] == "div":
                if num2 ==0:
                    return "You cannot divide by 0 you moron!"
                else:
                    return str(div(num1, num2))
            else:
                return "Operation not found!"

def getURLs(filepath):
    fd = open(filepath)
    for line in fd.readline():
        urls = re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", line)
        print(urls)

def get_comandos():
    comandos = []
    for i in range(5):
        comando = input("type the command you want to run on the system >>> ")
        comandos.append(comando)
    print(comandos)
    return comandos

def executa_comandos(comandos):
    for comando in comandos:
        print(os.popen(comando).read())



def show_clients(clients):
    counter = 0
    for client in clients:
        print(f"{counter} = {client[1]}")
        counter += 1

def run_cmd(clients):
    show_clients(clients)
    client_id = int(input("[+] Choose the client >>> "))
    cmd = input("[+] cmd >>> ")
    socket_cli = clients[client_id][0]
    socket_cli.sendall(cmd.encode())
    result = socket_cli.recv(2048).decode()
    print(result)



def menu():
    print(""""
    Network Manager
    1) show clients
    2) exec cmd
    3) disconnect client
    """)

def get_ip():
    ips = os.popen("ipconfig").read()
    ips = ips.split('\n')
    for ip in ips:
        if "IPv4" in ip:
            final_ip = ip.split(':')
            final_ip = final_ip[1]
            print(final_ip)
    #print(ip)



if __name__ == "__main__":
    executa_threaded()