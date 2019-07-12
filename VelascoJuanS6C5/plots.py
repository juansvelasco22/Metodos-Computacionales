import numpy as np
import matplotlib.pylab as plt

tiempo0=np.genfromtxt("placat0.dat")
tiempo100=np.genfromtxt("placat100.dat")

plt.imshow(tiempo100)
plt.show()

plt.imshow(tiempo0)
plt.show()