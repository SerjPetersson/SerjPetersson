import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 
           'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

page = "https://www.transfermarkt.ru/spieler-statistik/wertvollstespieler/marktwertetop"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')


Player = pageSoup.find_all("table", {"class": "inline-table"})
Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})
Club = []
Value = []

length = len(Player)

for i in range(length):
    Club.append(Player[i].text)
    Value.append(Values[i].text)
    
df = pd.DataFrame({"Игрок":Club,"Стоимость":Value})
print(df) 

