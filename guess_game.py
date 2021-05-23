import random
import os
from socket import *
import threading


class Server(object):
    clients = []
    def __init__(self, addr, port):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((addr,port))
        self.server.listen(100)
        self.closed = False
        #self.clients = []
            
    def conn(self, client):
        while True:
            dados = client.recv(2048).decode()
            print(f"client >>> {dados}")
            if dados == "sair":
                client.close()
                break
            dados =  input("Sever >>> ")
            client.sendall(dados.encode())



    def __call__(self, *args, **kwargs):
        while True:
            client, addr = self.server.accept()
            Server.clients.append([client, addr])
            t = threading.Thread(target=self.conn, args=(client,))
            t.start()



##############################################################
#
# class Guess_Game(object):
#     games = 0
#     def __init__(self):
#         self.rand = random.randint(1,200)
#         self.tries = 0
#     Guess_Game.games += 1
#
#     def guess(self, guess):
#         try:
#             if guess == "exit":
#                 return 1
#
#             guess = int(guess)
#             self.tries += 1
#             if guess == self.rand:
#                 print(f"Acertou em motherfucking {self.tries} tentativas, you go gal!")
#                 return 1
#             elif guess < self.rand:
#                 print("Too Low motherfucker!!!")
#             else:
#                 print("Too high Motherfucker!!!")
#             return 2
#         except Exception as e:
#             print(e)
#             return 3
#
#
#
# # game = guess_game()
# # while True:
# #     guess = input("Guess the number >>> ")
# #     result = game.guess(guess)
# #     if result == 1:
# #         print(f"Game Over!!")
# #         break
#
#
