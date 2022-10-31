import socket
import time
import threading
from tkinter import *

root=Tk()
root.geometry("300x500")
root.config(bg="white")

def func():
    pass

def threadsendmsg():
    pass

startchatimage=PhotoImage(file='start.png')

buttons=Button(root,image=startchatimage,command=func,borderwidth=0)
buttons.place(x=90,y=10)

message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444)

sendmessageimg=PhotoImage(file='send.png')

sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
sendmessagebutton.place(x=260,y=440)

lstbx=Listbox(root,height=20,width=43)
lstbx.place(x=15,y=80)


root.mainloop()