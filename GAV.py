import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from tkinter import Label
import webbrowser

def open_vk():
    webbrowser.open_new("https://vk.com")
def open_git():
    webbrowser.open_new("https://github.com")
def open_avito():
    webbrowser.open_new("https://www.avito.ru")
def open_yt():
    webbrowser.open_new("https://www.youtube.com")
def open_twitch():
    webbrowser.open_new("https://www.twitch.tv")
def open_deepl():
    webbrowser.open_new("https://www.deepl.com/translator")
def open_google():
    webbrowser.open_new("https://www.google.ru/?hl=ru")
def open_tg():
    webbrowser.open_new("https://web.telegram.org/")
def open_ds():
    webbrowser.open_new("https://discord.com")

# Создаем окно
okno = tk.Tk()
okno.title("                                                                                                                                                                    Система хранения необходимых ссылок")
okno.geometry("1280x720")
# Создаем виджет вкладок
tab_control = ttk.Notebook(okno)
# Создаем вкладку "Сайты"
vkladka_saitov = ttk.Frame(tab_control)
tab_control.add(vkladka_saitov, text='  Сайты  ')

frame = Frame(vkladka_saitov, bg='#007FFF')
frame.place(relx=0.15, rely=0.1, relwidth=0.1, relheight=0.2)
label = Label(frame, text="Вконтакте", font=("Arial", 10), bg="#007FFF", fg="azure2")
label.place(relx=0.27, rely=0.1)
btn = ttk.Button(vkladka_saitov, text="Открыть",  command=open_vk)
btn.place(relx=0.1724, rely=0.21)

frame = Frame(vkladka_saitov, bg='gray11')
frame.place(relx=0.45, rely=0.1, relwidth=0.1, relheight=0.2)
label = Label(frame, text="GitHub", font=("Arial", 10), bg="gray11", fg="azure2")
label.place(relx=0.34, rely=0.1)
btn = ttk.Button(vkladka_saitov,text="Открыть", command=open_git)
btn.place(relx=0.4724, rely=0.21)

frame = Frame(vkladka_saitov, bg='#66CD00')
frame.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.2)
label = Label(frame, text="Avito", font=("Arial", 10), bg="#66CD00", fg="azure2")
label.place(relx=0.385, rely=0.1)
btn = ttk.Button(vkladka_saitov,text="Открыть", command=open_avito)
btn.place(relx=0.7724, rely=0.21)

frame = Frame(vkladka_saitov, bg='#FF4040')
frame.place(relx=0.15, rely=0.39, relwidth=0.1, relheight=0.2)
label = Label(frame, text="YouTube", font=("Arial", 10), bg="#FF4040", fg="azure2")
label.place(relx=0.29, rely=0.1)
btn = ttk.Button(vkladka_saitov,text="Открыть", command=open_yt)
btn.place(relx=0.1724, rely=0.5)

frame = Frame(vkladka_saitov, bg='#9A32CD')
frame.place(relx=0.45, rely=0.39, relwidth=0.1, relheight=0.2)
label = Label(frame, text="Twitch", font=("Arial", 10), bg="#9A32CD", fg="azure2")
label.place(relx=0.35, rely=0.1)
btn = ttk.Button(vkladka_saitov,text="Открыть", command=open_twitch)
btn.place(relx=0.4724, rely=0.5)

frame = Frame(vkladka_saitov, bg='#104E8B')
frame.place(relx=0.75, rely=0.39, relwidth=0.1, relheight=0.2)
label = Label(frame, text="Deepl", font=("Arial", 10), bg="#104E8B", fg="azure2")
label.place(relx=0.35, rely=0.1)
btn = ttk.Button(vkladka_saitov,text="Открыть", command=open_deepl)
btn.place(relx=0.7724, rely=0.5)

frame = Frame(vkladka_saitov, bg='#FF7D40')
frame.place(relx=0.15, rely=0.68, relwidth=0.1, relheight=0.2)
label = Label(frame, text="Google", font=("Arial", 10), bg="#FF7D40", fg="azure2")
label.place(relx=0.32, rely=0.1)
btn = ttk.Button(vkladka_saitov,text="Открыть", command=open_google)
btn.place(relx=0.1724, rely=0.79)

frame = Frame(vkladka_saitov, bg='#1C86EE')
frame.place(relx=0.45, rely=0.68, relwidth=0.1, relheight=0.2)
label = Label(frame, text="Telegram", font=("Arial", 10), bg="#1C86EE", fg="azure2")
label.place(relx=0.28, rely=0.1)
btn = ttk.Button(vkladka_saitov,text="Открыть", command=open_tg)
btn.place(relx=0.4724, rely=0.79)

frame = Frame(vkladka_saitov, bg='#1874CD')
frame.place(relx=0.75, rely=0.68, relwidth=0.1, relheight=0.2)
label = Label(frame, text="Discord", font=("Arial", 10), bg="#1874CD", fg="azure2")
label.place(relx=0.325, rely=0.1)
btn = ttk.Button(vkladka_saitov,text="Открыть", command=open_ds)
btn.place(relx=0.7724, rely=0.79)


# Создаем вкладку "Пароли"
vkladka_paroli = ttk.Frame(tab_control)
tab_control.add(vkladka_paroli, text='  Пароли  ')

def copy_vk(event):
    password = "123QWERT"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()
def copy_git(event):
    password = "VbVgZxkmC"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()
def copy_avito(event):
    password = "tAvJWVaaJ"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()
def copy_yt(event):
    password = "glIWKaPgK"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()
def copy_twitch(event):
    password = "QsofnIuPkw"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()
def copy_deepl(event):
    password = "ggxIrXaReW"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()
def copy_google(event):
    password = "RiIkSRLn"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()
def copy_tg(event):
    password = "NAIBKMOQZwK"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()
def copy_ds(event):
    password = "065GecwVe1G"
    okno.clipboard_clear()
    okno.clipboard_append(password)
    okno.update()

label_vk = tk.Label(vkladka_paroli, text="Вконтакте:")
label_vk.pack()
label_vkpass = tk.Label(vkladka_paroli, text="123QWERT", fg="blue", cursor="hand2")
label_vkpass.pack()
label_vkpass.bind("<Button-1>", copy_vk)

label_git = tk.Label(vkladka_paroli, text="GITHub:")
label_git.pack()
label_gitpass = tk.Label(vkladka_paroli, text="VbVgZxkmC", fg="blue", cursor="hand2")
label_gitpass.pack()
label_gitpass.bind("<Button-1>", copy_git)

label_avito = tk.Label(vkladka_paroli, text="Avito:")
label_avito.pack()
label_avitopass = tk.Label(vkladka_paroli, text="tAvJWVaaJ", fg="blue", cursor="hand2")
label_avitopass.pack()
label_avitopass.bind("<Button-1>", copy_avito)

label_yt = tk.Label(vkladka_paroli, text="YouTube:")
label_yt.pack()
label_ytpass = tk.Label(vkladka_paroli, text="glIWKaPgK", fg="blue", cursor="hand2")
label_ytpass.pack()
label_ytpass.bind("<Button-1>", copy_yt)

label_twitch = tk.Label(vkladka_paroli, text="Twitch:")
label_twitch.pack()
label_twitchpass = tk.Label(vkladka_paroli, text="QsofnIuPkw", fg="blue", cursor="hand2")
label_twitchpass.pack()
label_twitchpass.bind("<Button-1>", copy_twitch)

label_deepl = tk.Label(vkladka_paroli, text="Deepl:")
label_deepl.pack()
label_deeplpass = tk.Label(vkladka_paroli, text="ggxIrXaReW", fg="blue", cursor="hand2")
label_deeplpass.pack()
label_deeplpass.bind("<Button-1>", copy_deepl)

label_google = tk.Label(vkladka_paroli, text="Google:")
label_google.pack()
label_googlepass = tk.Label(vkladka_paroli, text="RiIkSRLn", fg="blue", cursor="hand2")
label_googlepass.pack()
label_googlepass.bind("<Button-1>", copy_google)

label_tg = tk.Label(vkladka_paroli, text="Telegram:")
label_tg.pack()
label_tgpass = tk.Label(vkladka_paroli, text="NAIBKMOQZwK", fg="blue", cursor="hand2")
label_tgpass.pack()
label_tgpass.bind("<Button-1>", copy_tg)

label_ds = tk.Label(vkladka_paroli, text="Discord:")
label_ds.pack()
label_dspass = tk.Label(vkladka_paroli, text="065GecwVe1G", fg="blue", cursor="hand2")
label_dspass.pack()
label_dspass.bind("<Button-1>", copy_ds)

def search_keyword():
    keyword = entry_keyword.get()
    if keyword.lower() == "вконтакте":
        result = "123QWERT"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    elif keyword.lower() == "github":
        result = "VbVgZxkmC"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    elif keyword.lower() == "avito":
        result = "tAvJWVaaJ"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    elif keyword.lower() == "youtube":
        result = "glIWKaPgK"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    elif keyword.lower() == "twitch":
        result = "QsofnIuPkw"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    elif keyword.lower() == "deepl":
        result = "ggxIrXaReW"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    elif keyword.lower() == "google":
        result = "RiIkSRLn"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    elif keyword.lower() == "telegram":
        result = "NAIBKMOQZwK"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    elif keyword.lower() == "discord":
        result = "065GecwVe1G"
        label_result.config(text=result)
        okno.clipboard_clear()
        okno.clipboard_append(result)
        okno.update()
    else:
        result = "Ключевое слово не найдено"
        label_result.config(text=result)


entry_keyword = tk.Entry(vkladka_paroli)
entry_keyword.place(x=20, y=20)
button_search = tk.Button(vkladka_paroli, text="Найти", command=search_keyword)
button_search.place(x=20, y=50)
label_result = tk.Label(vkladka_paroli, text=" ")
label_result.place(x=20, y=80)

# Размещаем виджет вкладок в окне
tab_control.pack(expand=1, fill="both")
okno.mainloop()
