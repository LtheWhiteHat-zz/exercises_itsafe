from tkinter import *
import os


#business logic setup
#execute the command
def execute_cmd():
    cmd = inp_cmd.get()
    result = os.popen(cmd).read()
    output.insert(END, result)



#UI Setup
window = Tk()
window.title("L The White Hat OS command executor")
window.geometry("500x400")
window.iconbitmap('hacking.ico')
window.resizable(False, False)

lbl_cmd = Label(window, text="cmd to exe: ")
lbl_cmd.place(x=10, y=5)
inp_cmd = Entry(window, width=30)
inp_cmd.place(x=100, y=5)
btn_exec = Button(window, text="Execute!", command=execute_cmd)
btn_exec.place(x=300, y=5)

lbl__output = Label(window, text="Output: ")
output = Text(window, width=400)
output.place(x=5, y=30)

window.mainloop()