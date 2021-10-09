import csv
from tkinter import *
import requests
import codecs
from contextlib import closing
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import filedialog


root=Tk()
root['bg'] = '#3f6565'
root.title('Землетрясения за последний час') 
root.resizable(True, True)
root.geometry('800x500')
TableMargin = Frame(root, width=400)
TableMargin.pack(expand=True)

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Время","Место","Магнитуда землетрясения" ), height=200, selectmode="extended",
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y, expand=True)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X, expand=True)



tree.heading('Время', text="Время", anchor=W)
tree.heading('Место', text="Место", anchor=W)
tree.heading('Магнитуда землетрясения', text="Магнитуда землетрясения", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=150)
tree.column('#2', stretch=NO, minwidth=0, width=250)
tree.column('#3', stretch=NO, minwidth=0, width=170)
tree.pack()

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"

with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
    next(reader)
    for row in reader:
        date = row[0]
        place = row[13]
        mg = row[4]
        tree.insert("", 0, values=(date,place,mg))


def about_us():
                tkinter.messagebox.showinfo('Информация о землетрясениях', 'Программа написана на Python')

menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Помощь", menu=subMenu)
subMenu.add_command(label="О программе", command=about_us)
        

root.mainloop()        
