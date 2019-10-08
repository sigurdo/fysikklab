from eksternlab import height,slope,curvature #Må pip install eksternlab.
import numpy as np

x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
y = [0.278, 0.151, 0.08, 0.055, 0.078, 0.151, 0.275] #Høydene vi målte på labben

h = height(x, y)
print("h:", h)

x_interp = np.linspace(0.0, 1.2,50) #Er lengde fra til med antall intervaller
<<<<<<< HEAD
print("x_interp:", x_interp, len(x_interp))
=======
print("x_interp:", x_interp, len(x_interp))
>>>>>>> 0f7b3b7c0710182376575fc807ed6b7183c92cba
y_interp = h(x_interp)
print("y_interp:", y_interp, len(y_interp))

alpha = slope(h, x_interp) #Hellingsvinkelen til banen

kappa = curvature(h, x_interp) # Krumningsradiusen til banen.

for i in range(len(alpha)):
    print("Alfa:", alpha[i], "Kappa:", kappa[i])
