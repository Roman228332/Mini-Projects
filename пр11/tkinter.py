import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

window = tk.Tk()
window.title('Потапов Роман Михайлович')
window.geometry('660x430')
window['bg']='green'

ntb = ttk.Notebook(window)
ntb.pack(pady=10, padx=10)

tb1 = ttk.Frame(ntb)
tb2 = ttk.Frame(ntb)
tb3 = ttk.Frame(ntb)

ntb.add(tb1, text='калькулятор')
ntb.add(tb2, text='чекбоксы')
ntb.add(tb3, text='текст')

#1
def calculyator():
    chislo1 = entry1.get()
    chislo2 = entry2.get()
    deistvie = combo.get()
    if deistvie == '+':
        otvet = int(chislo1) + int(chislo2)
        entry3.delete(0, tk.END)
        entry3.insert(0, otvet)
    elif deistvie == '-':
        otvet = int(chislo1) - int(chislo2)
        entry3.delete(0, tk.END)
        entry3.insert(0, otvet)
    elif deistvie == '*':
        otvet = int(chislo1) * int(chislo2)
        entry3.delete(0, tk.END)
        entry3.insert(0, otvet)
    else:
        otvet = int(chislo1) / int(chislo2)
        entry3.delete(0, tk.END)
        entry3.insert(0, otvet)

entry1 = tk.Entry(tb1, width=6)
entry1.grid(row=0, column=0)

combo = ttk.Combobox(tb1, width=3)
combo['values'] = ('+', '-', '*', '/')
combo.current(0)
combo.grid(row=0, column=1)

entry2 = tk.Entry(tb1, width=6)
entry2.grid(row=0, column=2)

button1 = tk.Button(tb1, text='=', command=calculyator)
button1.grid(row=0, column=3)

entry3 = tk.Entry(tb1, width=6)
entry3.grid(row=0, column=4)

#2
def checkbox():
    message = ''
    if c1.get() == 1:
        message += '1             '
    if c2.get() == 1:
        message += '2             '
    if c3.get() == 1:
        message += '3             '
    messagebox.showinfo('вы выбрали:', message)

c1 = tk.IntVar()
c2 = tk.IntVar()
c3 = tk.IntVar()

check1 = tk.Checkbutton(tb2, text='первый', variable=c1)
check1.grid(pady=1, padx=1)

check2 = tk.Checkbutton(tb2, text='второй', variable=c2)
check2.grid(pady=2, padx=1)


check3 = tk.Checkbutton(tb2, text='третий', variable=c3)
check3.grid(pady=3, padx=1)

button2 = tk.Button(tb2, text='проверить', command=checkbox)
button2.grid(pady=50, padx=1)

#3
def fileopen():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r', encoding='utf-8') as file:
        txt.insert(tk.END, file.read())
menu = tk.Menu(window)
window.config(menu=menu)

file = tk.Menu(menu)
menu.add_cascade(label='файл', menu=file)
file.add_command(label='открыть', command=fileopen)

txt = tk.Text(tb3, wrap='word')
txt.pack(fill='both', expand=True)

window.mainloop()