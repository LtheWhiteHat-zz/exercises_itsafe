from tkinter import *
from guess_game import *


#business logic part
num_clients = 1
clients = []
#list clients
def add_client():
    global clients
    global num_clients
    client = entrada.get()
    num_clients += 1
    txt_list_clients.insert(num_clients, client)


def list_clients():
    global server
    global num_clients
    print(server.clients)
    for client in server.clients:
        txt_list_clients.insert(num_clients, client[0])
        print(client)

def end_program():
    exit(10)

# GUI Setup
window =Tk()
window.title("L The White Hat C&C Center")
window.geometry("500x400")
window.iconbitmap('hacking.ico')
window.resizable(False, False)

#menu
menu = Menu(window)

itens = Menu(menu)
itens.add_command(label="start")
itens.add_command(label="Close", command=end_program)
menu.add_cascade(label="File", menu=itens)
window.config(menu=menu)


#list clients UI
lbl_list_servers = Label(window, text="Para listar os clients clique no botao abaixo!")
lbl_list_servers.place(x=5, y=5)
btn_list_clients = Button(window, text="List Clients", command=list_clients)
btn_list_clients.place(x=400, y=5)

lbl_list_of_clients = Label(window, text="The connected clients are :")
lbl_list_of_clients.place(x=5, y=170)
txt_list_clients = Listbox(window, selectmode=MULTIPLE)
for i in range(len(clients)):
    txt_list_clients.insert(i, str(clients[i]))

txt_list_clients.place(x=5,y=200)

#connect to client UI
lbl_enter_client_id = Label(window, text="Entre com o id do client")
lbl_enter_client_id.place(x=5,y=30)
btn_connect_to_client = Button(window, text="connect to client!")
btn_list_clients.place(x=400,y=30)


#manual add of client for testing

#connect to client UI
lbl_enter_client = Label(window, text="Entre com o ip do client")
lbl_enter_client.place(x=5,y=100)
entrada = Entry(window, width=30)
entrada.place(x=200, y=100)
btn_add_client = Button(window, text="Add a client!", command=add_client)
btn_add_client.place(x=400,y=100)


window.mainloop()





