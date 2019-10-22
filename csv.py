# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:30:16 2019

@author: Sigurd
"""

import csv

filnavn = "CSV/Klipp33.csv"
data = []
with open(filnavn) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=";")
    header = next(csvReader)
    header = next(csvReader)
    
    for datapoint in csvReader:
        values = [value for value in datapoint]
        data.append(values)
        
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "":
            data[i][j] = "0"
            
        ting = list(data[i][j])
        
        for k in range(len(ting)):
            if ting[k] == ",":
                ting[k] = "."
                
        ting = "".join(ting)
        data[i][j] = float(ting)

print(data)