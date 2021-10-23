import csv
import json
import pickle

with open('audi.csv') as f:
    reader=csv.DictReader(f)
    rows=list(reader)
with open('audi.json', 'w') as f:
     json.dump(rows, f)

with open('audi.json') as a:
    reader2=json.load(a)
with open('audi.pkl', 'wb') as a:
    pickle.dump(reader2, a)

with open('audi.pkl', 'rb') as x:
    reader3=pickle.load(x)
with open('123.json', 'w') as x:
    json.dump(reader3,x)