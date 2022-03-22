import csv
import operator
from tkinter import *
import requests
import codecs
from contextlib import closing
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import filedialog
import webbrowser

root=Tk()
root.title('Обнаруженные экзопланеты') 
root.resizable(True, True)
root.geometry('1120x500')
root['bg']='#2bcdee'
root.iconbitmap('exoplanet.ico')
TableMargin = Frame(root, width=400)
TableMargin.pack(expand=True)

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Название","Статус", "Радиус(Юпитера)","Метод открытия", "Дата обнаружения", "Дата обновления информации" ), height=200, selectmode="extended",
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y, expand=True)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X, expand=True)


tree.heading('Название', text="Название", anchor=W)
tree.heading('Статус', text="Статус", anchor=W)
tree.heading('Радиус(Юпитера)', text="Радиус(Юпитера)", anchor=W)
tree.heading('Метод открытия', text="Метод открытия", anchor=W)
tree.heading('Дата обнаружения', text="Дата обнаружения", anchor=W)
tree.heading('Дата обновления информации', text="Дата обновления информации", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=150)
tree.column('#2', stretch=NO, minwidth=0, width=250)
tree.column('#3', stretch=NO, minwidth=0, width=170)
tree.column('#4', stretch=NO, minwidth=0, width=170)
tree.column('#5', stretch=NO, minwidth=0, width=180)
tree.column('#6', stretch=NO, minwidth=0, width=180)
tree.pack()

exofile="http://exoplanet.eu/catalog/csv"

with closing(requests.get(exofile, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
    next(reader)
    a=sorted(reader, key=operator.itemgetter(25), reverse=False)
            
    for row in a:
        name = row[0]
        status = row[1]
        radius = row[8]
        method = row[63]
        date1 = row[24]
        date2 = row[25]
        tree.insert('',0,values=(name,status,radius,method,date1,date2))
                                      
def about_us():
     tkinter.messagebox.showinfo('Информация об экзопланетах', 'Программа написана на Python')


   
def info():
    tkinter.messagebox.showinfo('Данные об экзопланетах', 'Всю информацию вы можете посмотреть на сайте http://exoplanet.eu/catalog/')

def sense():
    
   tkinter.messagebox.showinfo('Справочник', 'Радиус Юпитера = 69911 километров\n\nPrimary Transit - c помощью транзитов \
обнаруживаются экзопланеты не потому, что мы видим ее сквозь световые годы, а потому,\
что планета, проходящая перед своей звездой, слегка затемняет её.\nЭто затемнение можно увидеть на световых кривых - графиках, \
показывающих свет, накопленный от звезды за период наблюдения.\nКогда экзопланета проходит перед звездой, световая кривая показывает \
падение яркости звезды.\n\nRadial velocity - Доплеровская спектроскопия (также известная как метод радиальной скорости) - косвенный метод \
нахождения экзопланет и коричневых карликов из измерений радиальной скорости посредством наблюдения \
доплеровских сдвигов в спектре родительской звезды планеты.\n\nTiming - невидимые планеты могут стать известными под действием \
гравитационных тяг, которые они оказывают на другие планеты и звёзды. \
Эти буксиры вызывают вариации во времени предсказуемых событий, таких как планетарные переходы, двойные звездные затмения и \
естественные импульсы в излучении звезд. Наблюдая изменения времени, астрономы могут сделать вывод о присутствии другого мира.\n\n\
Microlensing - Метод гравитационного микролинзирования позволяет находить планеты с помощью света от далекой звезды. Путь света от \
этой звезды будет изменяться наличием массивной линзы - звезды и планеты.\nТаким образом, в течение короткого периода времени \
далекая звезда будет выглядеть ярче.\n\nImaging - прямая визуализация состоит из непосредственного захвата изображений экзопланет, \
что возможно путем поиска света, отраженного от атмосферы планеты на инфракрасных длинах волн.''')

                                    
def quantity():
    exofile1="http://exoplanet.eu/catalog/csv"
    rows = list(csv.DictReader(requests.get(exofile).text.splitlines()))
    tkinter.messagebox.showinfo("Количество", f"Найденных экзопланет: {len(rows)}")

def callback():
    url= 'http://exoplanet.eu/catalog'
    webbrowser.open(url)
    
menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Помощь", menu=subMenu)
subMenu.add_command(label="О программе", command=about_us)
subMenu.add_command(label="Информация", command=info)
   
subMenu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Справка", menu=subMenu1)
subMenu1.add_command(label="Значения в программе", command=sense)
subMenu1.add_command(label="Экзопланеты", command=quantity)

subMenu2 = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Сайт", menu=subMenu2)
subMenu2.add_command(label="Перейти на сайт", command = callback)


        
root.mainloop()        
