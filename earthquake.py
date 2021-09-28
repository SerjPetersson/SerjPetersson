import csv
import requests
import codecs
from contextlib import closing


csvurl = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv'
rows = list(csv.DictReader(requests.get(csvurl).text.splitlines()))
print("Количество зарегистрированных землятресений за последний час:", len(rows))

print('***********')
url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"

with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
    for row in reader:
        print(row[0],row[13],row[4])   





