#import numpy
import scipy
from eksternlab import height,slope,curvature #MÃ¥ pip install eksternlab.
import numpy as np
import buelengde as buelengde
import trackerData as trackerData
import matplotlib as plt
from pylab import *;plot();show()

x_track = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
for i in range(len(x_track)):
    x_track[i] *= 0.975
y_track = [0.278, 0.151, 0.08, 0.055, 0.078, 0.151, 0.275] #HÃ¸ydene vi mÃ¥lte pÃ¥ labben

h = height(x_track, y_track)
print("h:", h)

x_interp = np.linspace(0.0, 1.2,50) #Er lengde fra til med antall intervaller
print("x_interp:", x_interp, len(x_interp))
y_interp = h(x_interp)
print("y_interp:", y_interp, len(y_interp))

alpha = slope(h, x_interp) #Hellingsvinkelen til banen

kappa = curvature(h, x_interp) # Krumningsradiusen til banen.
kappa[0] = kappa[1]

for i in range(len(alpha)):
    print("x:", "{:1.3f}".format(x_interp[i]), "y:", "{:1.3f}".format(y_interp[i]), "Alfa:", "{:1.3f}".format(alpha[i]), "Kappa:", "{:1.3f}".format(kappa[i]))

totaltid = 40
iterasjoner = 5000

a = [0]
v = [0.5]
s = [0]
x = [0]
f = [0]
N = [0.3]

g = 9.81
k = 0.00424
m = 0.03
c = 2/5
dt = totaltid/iterasjoner

def aks(n):
    a_n = (g * np.sin(alpha[buelengde.getIndex(s[n-1], x_interp, y_interp, alpha)]) - (k / m) * v[n-1]) / (1 + c)
    a.append(a_n)
    return a_n

def vel(n):
    v_n = v[n-1] + a[n] * dt
    v.append(v_n)
    return v[n]

def spa(n): #spa står for spatium som betyr avstand på latin
    s_n = s[n-1] + v[n] * dt
    s.append(s_n)
    return s[n]

def pos(n):
    x_n = x[n-1] + v[n] * np.cos(alpha[buelengde.getIndex(s[n-1], x_interp, y_interp, alpha)]) * dt
    x.append(x_n)
    return x[n]

def fri(n):
    i = buelengde.getIndex(s[n], x_interp, y_interp, alpha)
    f_n = 2/7 * (m * g * np.sin(alpha[i]) - k * v[n])
    f.append(f_n)
    return f[n]

def nor(n):
    i = buelengde.getIndex(s[n], x_interp, y_interp, alpha)
    N_n = m * (g * np.cos(alpha[i]) + v[n]**2 / kappa[i])
    N.append(N_n)
    return N[n]

def euler():
    for n in range(1, iterasjoner):
        aks(n)
        vel(n)
        spa(n)
        pos(n)
        fri(n)
        nor(n)
        #if n < 200:
            #print("a = {:1.3f}".format(a[n]))
            #print("v = {:1.3f}".format(v[n]))
            #print("s = {:1.3f}".format(s[n]))

euler()

t = [0]
for i in range(1, iterasjoner):
    t.append(t[i-1]+dt)

"""x = []
for i in range(iterasjoner):
    x.append(buelengde.getX(s[i], x_interp, y_interp, alpha))"""

tStart = []
xStart = []
for i in range(200):
    tStart.append(t[i])
    xStart.append(x[i])
    
    
malingData = trackerData.getData("CSV/Klipp33test.csv")

tOffset = malingData[0][0]
xOffset = malingData[0][1]
for i in range(len(malingData)):
    malingData[i][0] = malingData[i][0] - tOffset
    malingData[i][1] = malingData[i][1] - xOffset

tData = []
xData = []
for i in range(len(malingData)):
    tData.append(malingData[i][0])
    xData.append(malingData[i][1])

tDataStart = []
xDataStart = []
for i in range(200):
    tDataStart.append(tData[i])
    xDataStart.append(xData[i])

#plt = matplotlib.pyplot.figure(figsize=(15.0, 10.0))

thingsToPlot = ["pos", "forces", "vel"]
thingToPlot = thingsToPlot[2]

if thingToPlot == "pos":
    kort = 0
    if kort:
        plt.plot(tStart, xStart)
        plt.plot(tDataStart, xDataStart)
    else:
        plt.plot(t, x)
        plt.plot(tData, xData)
    
    plt.ylabel("x-posisjon[m]")
    plt.legend(["Teoretisk", "Eksperimentelt"])

elif thingToPlot == "forces":
    kort = 0
    if kort:
        tStart = []
        fStart = []
        NStart = []
        for n in range(int(iterasjoner*0), int(iterasjoner*0.1)):
            tStart.append(t[n])
            fStart.append(f[n])
            NStart.append(N[n])
        
        plt.plot(tStart, fStart)
        plt.plot(tStart, NStart)
    else:
        plt.plot(t, f)
        plt.plot(t, N)
    
    plt.ylabel("kraft[N]")
    plt.legend(["Rullefriksjon", "Normalkraft"])

elif thingToPlot == "vel":
    vAbs = []
    #for el in v:
    vAbs= np.abs(v)
    tData = []
    vData = []
    for i in range(len(malingData)):
        tData.append(malingData[i][0])
        vData.append(malingData[i][3])
    
    plt.plot(t, vAbs)
    plt.plot(tData, vData)
    
    plt.ylabel("fart[m/s]")
    plt.legend(["Teoretisk", "Eksperimentelt"])

plt.xlabel("tid[s]")

#plt.show()
plt.savefig("test.png")

print(x[len(x)-1], xData[len(xData)-1])