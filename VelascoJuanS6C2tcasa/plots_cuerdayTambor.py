import numpy as np
import matplotlib.pylab as plt

caso1=np.genfromtxt("datos1.dat", delimiter ="\t")
caso2=np.genfromtxt("datos2.dat", delimiter ="\t")
caso3=np.genfromtxt("datos3.dat", delimiter ="\t")

fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(131)
ax2=fig.add_subplot(132)
ax3=fig.add_subplot(133)

ax1.scatter(datos1, label="Caso 1")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Amplitud")


ax2.scatter(xcar,z, label="Caso 2")
ax2.set_xlabel("Amplitud")
ax2.set_ylabel("Tiempo")


ax3.scatter(ycar,z, label="Caso 3")
ax3.set_xlabel("Amplitud")
ax3.set_ylabel("Tiempo")


ax1.legend()
ax2.legend()
ax3.legend()

fig.savefig("plots_cuerdayTambor.png")