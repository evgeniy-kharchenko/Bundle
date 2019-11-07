#Calcuator
# импорт модулей

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()                             # создание окна
root.title("Calculator")                # название окна
                                        # создание списка кнопок
bttn_list = [

    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C"
]

r = 1
c = 0
                                        # цикл
for i in bttn_list:
    rel = ""
    cmd=lambda x=i:\
        ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c +=1
    if c>4:
        c=0
        r += 1

root.mainloop()


