from tkinter import *
from random import randint

root = Tk()
root.geometry("500x500")

def button_action():
    label2 = Label(root, text="KAKALAND")
    label2.place(x=randint(10,400), y=randint(10,400))

label = Label(root, text="Kaka", font=("consolas", 18, "bold"))
label.place(x=50, y=100)

button = Button(root, command=button_action, font=("consolas", 25))
button.pack()

root.mainloop()