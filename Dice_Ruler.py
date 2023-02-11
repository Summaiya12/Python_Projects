import random
from tkinter import *

root = Tk()
root.geometry("700x500")

l1 = Label(root, text='', font=("times", 200))

def roll():
    numbers = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(numbers)}{random.choice(numbers)}', bg="yellow")
    l1.pack()

b1 = Button(root, text="Click To Roll Dice", command=roll, bg="white")
b1.place(x=200, y=20)
b2 = Button(root, text="EXIT", command=quit, bg="red")
b2.place(x=400, y=20)

root.mainloop()