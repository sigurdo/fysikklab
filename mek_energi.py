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

m = 0.03 #massen til ballen i kilo vår veier 30 gram
g = 9.81 #gravitasjons konstaneten

v = [p[3]for p in data]
h = [p[2]for p in data]

mek_energi = []

for i in range(len(data)):
    energi = m*g* float(h[i])+0.7*m*(float(v[i]))**2
    mek_energi.append(energi)

print(mek_energi)

for i in range(len(mek_energi)-1):
    energi_tap=(mek_energi[i]-mek_energi[i+1])*100 #Regner ut energitapet per sekund.
print(energi_tap)
