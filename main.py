#import numpy
import scipy
from eksternlab import height,slope,curvature #MÃ¥ pip install eksternlab.
import numpy as np
import buelengde as buelengde
import matplotlib as plt
from pylab import *;plot();show()

x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
y = [0.278, 0.151, 0.08, 0.055, 0.078, 0.151, 0.275] #HÃ¸ydene vi mÃ¥lte pÃ¥ labben

h = height(x, y)
print("h:", h)

x_interp = np.linspace(0.0, 1.2,50) #Er lengde fra til med antall intervaller
print("x_interp:", x_interp, len(x_interp))
y_interp = h(x_interp)
print("y_interp:", y_interp, len(y_interp))

alpha = slope(h, x_interp) #Hellingsvinkelen til banen

kappa = curvature(h, x_interp) # Krumningsradiusen til banen.

for i in range(len(alpha)):
    print("x:", "{:1.3f}".format(x_interp[i]), "y:", "{:1.3f}".format(y_interp[i]), "Alfa:", "{:1.3f}".format(alpha[i]), "Kappa:", "{:1.3f}".format(kappa[i]))

totaltid = 45
iterasjoner = 5000

a = [0]
v = [0]
s = [0]

g = 9.81
k = 0.002
m = 0.005
c = 1
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

def euler():
    for n in range(1, iterasjoner):
        aks(n)
        vel(n)
        spa(n)
        #if n < 200:
            #print("a = {:1.3f}".format(a[n]))
            #print("v = {:1.3f}".format(v[n]))
            #print("s = {:1.3f}".format(s[n]))

euler()

plt.plot(range(iterasjoner), s)
plt.show()