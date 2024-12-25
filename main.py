from tkinter import *
from tkinter import messagebox
import subprocess

top = Tk()

top.geometry("300x300")
myLabel = Label(top, text="Restart the computer!")
myLabel.pack()

def helloCallBack():
   subprocess.call(["shutdown", "-r", "-t", "0"])


B = Button(top, text ="Restart", command = helloCallBack)
B.place(x=115,y=115)
top.mainloop()