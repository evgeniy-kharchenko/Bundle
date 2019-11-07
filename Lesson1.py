#Calcuator
# импорт модулей

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()                             # создание окна
root.title("Calculator")                # название окна
                                        # создаем логику калькулятора
# создание функции calc с параметром key     
# создание глобальной переменной (работает вне функции) global
def calc(key):
    global memory                       # создание глобальной переменной (работает вне функции) global
    if key == "=":
# исключение ввода недопустимых символов в калькулятор
        str1= "-+0123456789.*/"         
        if calc_entry.get()[0] not in str1:
            calc_entry.insert (END, "Не подходящий символ")
            messagebox.showerror("Error!")
# счет
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error")
            messagebox.showerror("Error", "Check the data")
# очистка поля ввода
    elif key == "C":
        calc_entry.delete(0, END)
# смена + - символов
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
                                    
                                        # создание списка кнопок
bttn_list = [

    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C"
            ]

r = 1                                   # переменные для счета
c = 0                                   # переменная для счета
                                        # цикл
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1 
    if c>4:
        c=0
        r += 1

calc_entry = Entry(root, width=33)                  # создание окна ввода
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()                         # замыкаем луп - действие кулькулятора

# link to exercise: https://www.youtube.com/watch?v=9JlEi_1iHKs&t=712s