import numpy as np
import matplotlib.pylab as plt

def mifun(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)

pasos=[]
iteraciones=1000


def MH(numpasos,sigma):
    pasos=np.array([])
    xviejo=np.random.uniform(-4,4,1)
    pasos=np.append(pasos,xviejo)
    
    for i in range(numpasos):
        xnuevo=np.random.normal(pasos[i],sigma)
        
        alpha=mifun(xnuevo)/mifun(pasos[i])
        if(alpha>=1):
            pasos=np.append(pasos,xnuevo)
        else:
            beta=np.random.random()
            if(beta<alpha):
                pasos=np.append(pasos,xnuevo)
            else:
                pasos=np.append(pasos,xviejo)
    return pasos


caso1=MH(100000,5)
plt.hist(caso1, bins=1000, density=True)
plt.plot(x,funcion)
plt.show()

caso2=MH(100000,0.2)
plt.hist(caso2, bins=1000, density=True)
plt.plot(x,funcion)
plt.show()

caso3=MH(100000,0.01)
plt.hist(caso3, bins=1000, density=True)
plt.plot(x,funcion)
plt.show()

caso4=MH(1000,0.1)
plt.hist(caso4, bins=1000, density=True)
plt.plot(x,funcion)
plt.show()

caso5=MH(100000,0.1)
plt.hist(caso5, bins=1000, density=True)
plt.plot(x,funcion)
plt.show()
