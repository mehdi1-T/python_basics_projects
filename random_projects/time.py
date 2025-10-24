from tkinter import *
import time

user = time.ctime()

root = Tk()
root.geometry("500x500")
root.config(bg="#662D91")

lbl = Label(root, text=user,bg="#662D91",fg='white',font=("impact",35,"bold"))
lbl.pack(expand=True)
lbl.pack(anchor="center")


root.mainloop()