import os
from tkinter import *

def rename():
    folder_path = r''+path.get()
    counter = 1
    for filename in os.listdir(folder_path):
        os.rename(folder_path+'\\'+filename, folder_path+'\\'+word.get()+str(counter)+exe.get())
        counter = counter+1
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0, END)

root = Tk()
root.title('RENAMER')
root.geometry('300x300')
path = StringVar()
Label(root,text='PASTE FILE PATH', font=('TIMES ROMAN',12)).pack()
ent1 = Entry(root,textvariable=path ,font=('TIMES ROMAN',12))
ent1.pack()

word= StringVar()
Label(root,text='GIVE ONE WORD', font=('TIMES ROMAN',12)).pack()
ent2 = Entry(root,textvariable=word ,font=('TIMES ROMAN',12))
ent2.pack()

exe= StringVar()
Label(root,text='ENTER EXTENSION', font=('TIMES ROMAN',12)).pack()
ent3 = Entry(root,textvariable=exe ,font=('TIMES ROMAN',12))
ent3.pack()

Button(root,text='change',command=rename).pack()
root.mainloop()