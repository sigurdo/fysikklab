from eksternlab import height,slope,curvature #Må pip install eksternlab.
import numpy as np

x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
y = [0.278, 0.151, 0.08, 0.055, 0.078, 0.151, 0.275] #Høydene vi målte på labben

h = height(x, y)

x_interp = np.linspace(0.278, 0.151) #Litt usikker på hva som skal være her.
y_interp = h(x_interp)

alpha = slope(h, x_interp) #Hellingsvinkelen til banen
print(alpha)

kappa = curvature(h, x_interp) # Krumningsradiusen til banen.

print(kappa)
