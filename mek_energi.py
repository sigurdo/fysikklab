import csv
from decimal import Decimal
filename = "test.csv" #Skriv inn navn til csv-fil

data = []

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";")

    header = next(csvreader)

    for datapoint in csvreader:


        values = [value for value in datapoint]
        data.append(values)

m = 1 #massen til ballen i kilo
g = 9.81 #gravitasjons konstaneten

v = [p[3]for p in data]
h = [p[2]for p in data]

mek_energi = [] #liste med det mekaniske energien

for i in range(len(data)):
    energi = m*g* float(h[i])+0.7*m*(float(v[i]))**2 # renger ut mekanisk energi
    mek_energi.append(energi)

print(mek_energi)
