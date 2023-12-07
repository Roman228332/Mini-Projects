import tkinter as tk
import requests
import json


def func_json():
    name = ent.get()
    ssylka = f'https://api.github.com/repos/{name}'
    dannye = requests.get(ssylka).json()
    information = ['company', 'created_at', 'email', 'id', 'name', 'url']
    dict = {}
    for x in information:
        if x in list(dannye.keys()):
            dict[x] = dannye[x]
        else:
            dict[x] = "none"

    file = open('Json.json', 'w')
    json.dump(dict, file, indent=1)


window = tk.Tk()
window.title('Потапов Роман Михайлович')
window.geometry('1280x720')
window.configure(bg='grey')

text = tk.Label(window, text='Введите имя репозитория')
text.pack()

stroka_vvoda = tk.Entry(window)
stroka_vvoda.pack()

knopka = tk.Button(window, text='Получить информацию', command=func_json)
knopka.pack()
window.mainloop()