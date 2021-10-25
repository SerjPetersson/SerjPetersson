import requests 
import csv
import codecs
from contextlib import closing


exofile="http://exoplanet.eu/catalog/csv"
rows = list(csv.DictReader(requests.get(exofile).text.splitlines()))
print("Количество найденных экзопланет:", len(rows))

with closing(requests.get(exofile, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
    next(reader)
    for row in reader:
        print(row[0],row[1],row[8],row[24], row[25])


