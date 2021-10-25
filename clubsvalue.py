import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 
           'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

page = "https://www.transfermarkt.ru/spieler-statistik/wertvollstemannschaften/marktwertetop"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')


Clubs = pageSoup.find_all("td", {"class": "no-border-links hauptlink"})
Values = pageSoup.find_all("td", {"class": "rechts"})
Club = []
Value = []

length = len(Clubs)

for i in range(length):
    Club.append(Clubs[i].text)
    Value.append(Values[i].text)
    
df = pd.DataFrame({"Клубы":Club,"Стоимость":Value})
print(df) 

