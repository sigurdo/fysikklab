#import numpy
import scipy
from eksternlab import height,slope,curvature #MÃ¥ pip install eksternlab.
import numpy as np
import buelengde

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

a = []
v = []
s = []

def euler():
    for n in range(1000):
        i = 0
        #while x_interp[i] < s[n]

#input()