import csv
filename="" #Skriv inn navn til csv-fil

with open(filename) as csvfile: 
    csvreader=csv.reader(csvfile)

    header =next(csvreader)

    for datapoint in csvreader:

        values=[float(value) for value in datapoint]

        data.append(values)

m #massen til ballen.
g=9.81 #gravitasjons konstaneten

v=[p[3]for p in data]
h=[p[2]for p in data]

mek_energi=[]

for i in range(len(data)):
    energi=m*g*h[i]]+0.5*m*(v[i])**2+7/10*m*(v[i])**2
    energi.append(mek_energi)
