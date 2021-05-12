from tkinter import *
from tkinter import messagebox
import calendar
import datetime
from ttkthemes import themed_tk as tk
from tkinter import ttk


root = tk.ThemedTk()
root.get_themes()
root.set_theme("yaru")
root.title('Календарь')
root.resizable(False, False)

days = []
now = datetime.datetime.now()
year = now.year
month = now.month


    
mainmenu=Menu(root)
root.config(menu=mainmenu)
fileMenu = Menu(mainmenu,tearoff=0)
fileMenu.add_command(label="Выход", command=root.destroy)
mainmenu.add_cascade(label="Файл", menu=fileMenu)
helpmenu = Menu(mainmenu, tearoff=0)

def about():
    messagebox.showinfo('Инфо', "Эта программа написана на Python")
    
helpmenu.add_command(label="О программе", command=about)
mainmenu.add_cascade(label="Справка", menu=helpmenu)


def prew():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()

def tonext():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()
    
def fill():
    info_label['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        prew_month_days = calendar.monthrange(year-1, 12)[1]
    else:
        prew_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]
    for n in range(month_days):
        days[n + week_day]['text'] = n
        days[n + week_day]['fg'] = 'gray'
        if year == now.year and month == now.month and n == now.day:
            days[n + week_day]['background'] = 'light goldenrod'
        else:
            days[n + week_day]['background'] = 'mint cream'
    for n in range(week_day):
        days[week_day - n - 1]['text'] = prew_month_days - n
        days[week_day - n - 1]['fg'] = 'light cyan'
        days[week_day - n - 1]['background'] = 'snow3'
    for n in range(6*7 - month_days - week_day):
        days[week_day + month_days + n]['text'] = n+1
        days[week_day + month_days + n]['fg'] = 'gray50'
        days[week_day + month_days + n]['background'] = 'ivory2'

prew_button = ttk.Button(root, text='<', command=prew)
prew_button.grid(row=0, column=0, sticky='nsew')
next_button = ttk.Button(root, text='>', command=tonext)
next_button.grid(row=0, column=6, sticky='nsew')
info_label = Label(root, text='0', width=1, height=1, 
            font=('Verdana', 16, 'bold'), fg='plum3')
info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

for n in range(7):
    lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1, 
                font=('Verdana', 10, 'normal'), fg='purple3')
    lbl.grid(row=1, column=n, sticky='nsew')
    
for row in range(6):
    for col in range(7):
        lbl = Label(root, text='0', width=4, height=2, 
                    font=('Verdana', 16, 'bold'))
        lbl.grid(row=row+2, column=col, sticky='nsew')
        days.append(lbl)
fill()
root.mainloop()

