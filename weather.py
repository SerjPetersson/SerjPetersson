from tkinter import *
import requests
from ttkthemes import themed_tk as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk

root = tk.ThemedTk()
root.set_theme("keramik")
root.geometry('500x500')
root['bg'] = '#3f6565'
root.title('Температура в городе')
APIKEY='73bc31bbbdeb991500796c93a5f2256a'

def get_weather():
        city = cityField.get()
        key = APIKEY
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': city, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()
        icon = weather['weather'][0]['icon']
        info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}°'
                              
frame_top = Frame(root, bg='#b8fff2', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#b8fff2', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='#e0e0e0', font=30)
cityField.pack() 

btn = ttk.Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

info = Label(frame_bottom, text='Температура', bg='#b8fff2')
info.pack()

def about_us():
                tkinter.messagebox.showinfo('Погодное приложение на Python', 'Название города напишите на английском языке, затем нажмите на кнопку "посмотреть погоду"')

menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Помощь", menu=subMenu)
subMenu.add_command(label="Инструкция", command=about_us)

root.mainloop()

