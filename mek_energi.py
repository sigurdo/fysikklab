import csv
import numpy
import random
import trackerData as trackerData
import Feil as Feil
from scipy.integrate import simps
from decimal import Decimal
k=[]
for fil in range(33, 39):
    filnavn="Klipp"+str(fil)+".csv"
    filename = filnavn #Skriv inn navn til csv-fil

    data = trackerData.getData("CSV/"+filename)

    # with open(filename) as csvfile:
    #     csvreader = csv.reader(csvfile, delimiter=";")

    #     header = next(csvreader)

    #     for datapoint in csvreader:


    #         values = [value for value in datapoint]
    #         data.append(values)

    m = 0.03 #massen til ballen i kilo vår veier 30 gram
    g = 9.81 #gravitasjons konstaneten

    v = [p[3]for p in data]
    h = [p[2]for p in data]

    mek_energi = []

    for i in range(len(data)):
        energi = m*g* float(h[i])+0.7*m*(float(v[i]))**2
        mek_energi.append(energi)

    fart_float=[]
    for test in range(len(v)):
        mid=float(v[test])
        fart_float.append(pow(mid, 2))
    #print(fart_float)
    print("Integral")
    #print("fart_float:", fart_float)
    integral=numpy.trapz(fart_float)
    print("integral:", integral)
    energi_tap=0
    for i in range(len(mek_energi)-1):
        energi_tap += (mek_energi[i+1]-mek_energi[i]) #Regner ut energitapet per sekund.

        
    print(energi_tap)

    print("k:"+str(-(energi_tap/integral)*100))

    k.append(-(energi_tap/integral)*100)

print("k_liste:", k)
print("Standar avvik" +str(Feil.standardavvik(k)))
def gjennomsnitt(k):
    total=0
    for element in k:
        total+=element
    
    return total/len(k)

print("Standarfeil" +str(Feil.standardfeil(gjennomsnitt(k),k)))
