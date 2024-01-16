import tkinter as tk
from tkinter import ttk
import webbrowser

def open_vk(event):
    webbrowser.open_new("https://vk.com")
def open_git(event):
    webbrowser.open_new("https://github.com")
def open_avito(event):
    webbrowser.open_new("https://www.avito.ru")
def open_yt(event):
    webbrowser.open_new("https://www.youtube.com")
def open_twitch(event):
    webbrowser.open_new("https://www.twitch.tv")
def open_deepl(event):
    webbrowser.open_new("https://www.deepl.com/translator")
def open_google(event):
    webbrowser.open_new("https://www.google.ru/?hl=ru")
def open_tg(event):
    webbrowser.open_new("https://web.telegram.org/")
def open_ds(event):
    webbrowser.open_new("https://discord.com")
def open_wiki(event):
    webbrowser.open_new("https://ru.wikipedia.org")

# Создаем окно
okno = tk.Tk()
okno.title("Система хранения необходимых ссылок")
okno.geometry("1280x720")
# Создаем виджет вкладок
tab_control = ttk.Notebook(okno)
# Создаем вкладку "Сайты"
vkladka_saitov = ttk.Frame(tab_control)
tab_control.add(vkladka_saitov, text='Сайты')

label_sites = tk.Label(vkladka_saitov, text="Ссылка на Вконтакте:")
label_sites.pack()
vk_link = tk.Label(vkladka_saitov, text="https://vk.com", fg="blue", cursor="hand2")
vk_link.bind("<Button-1>", open_vk)
vk_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на GITHub:")
label_sites.pack()
git_link = tk.Label(vkladka_saitov, text="https://github.com", fg="blue", cursor="hand2")
git_link.bind("<Button-1>", open_git)
git_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на Avito:")
label_sites.pack()
avito_link = tk.Label(vkladka_saitov, text="https://www.avito.ru", fg="blue", cursor="hand2")
avito_link.bind("<Button-1>", open_avito)
avito_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на YouTube:")
label_sites.pack()
yt_link = tk.Label(vkladka_saitov, text="https://www.youtube.com", fg="blue", cursor="hand2")
yt_link.bind("<Button-1>", open_yt)
yt_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на Twitch:")
label_sites.pack()
twitch_link = tk.Label(vkladka_saitov, text="https://www.twitch.tv", fg="blue", cursor="hand2")
twitch_link.bind("<Button-1>", open_twitch)
twitch_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на Deepl:")
label_sites.pack()
deepl_link = tk.Label(vkladka_saitov, text="https://www.deepl.com/translator", fg="blue", cursor="hand2")
deepl_link.bind("<Button-1>", open_deepl)
deepl_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на Google:")
label_sites.pack()
google_link = tk.Label(vkladka_saitov, text="https://www.google.ru/?hl=ru", fg="blue", cursor="hand2")
google_link.bind("<Button-1>", open_google)
google_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на Telegram:")
label_sites.pack()
tg_link = tk.Label(vkladka_saitov, text="https://web.telegram.org/", fg="blue", cursor="hand2")
tg_link.bind("<Button-1>", open_tg)
tg_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на Discord:")
label_sites.pack()
ds_link = tk.Label(vkladka_saitov, text="https://discord.com", fg="blue", cursor="hand2")
ds_link.bind("<Button-1>", open_tg)
ds_link.pack()

label_sites = tk.Label(vkladka_saitov, text="Ссылка на Wikipedia:")
label_sites.pack()
wiki_link = tk.Label(vkladka_saitov, text="https://ru.wikipedia.org", fg="blue", cursor="hand2")
wiki_link.bind("<Button-1>", open_wiki)
wiki_link.pack()

# Создаем вкладку "Пароли"
vkladka_paroli = ttk.Frame(tab_control)
tab_control.add(vkladka_paroli, text='Пароли')

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
def copy_wiki(event):
    password = "6HVd2f7F8E"
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

label_wiki = tk.Label(vkladka_paroli, text="Wikipedia:")
label_wiki.pack()
label_wikipass = tk.Label(vkladka_paroli, text="6HVd2f7F8E", fg="blue", cursor="hand2")
label_wikipass.pack()
label_wikipass.bind("<Button-1>", copy_wiki)

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
    elif keyword.lower() == "wikipedia":
        result = "6HVd2f7F8E"
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
label_result = tk.Label(vkladka_paroli, text="Результат поиска:")
label_result.place(x=20, y=80)

# Размещаем виджет вкладок в окне
tab_control.pack(expand=1, fill="both")
okno.mainloop()

