import numpy as np
import matplotlib.pylab as plt

def mifun(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)
x=np.linspace(-4,4,100)
funcion=mifun(x)
normal=funcion/np.trapz(funcion)
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
            beta=np.random.uniform()
            if(beta<alpha):
                pasos=np.append(pasos,xnuevo)
            else:
                pasos=np.append(pasos,pasos[i])
    return pasos


caso1=MH(100000,5)
caso2=MH(100000,0.2)
caso3=MH(100000,0.01)
caso4=MH(1000,0.1)
caso5=MH(100000,0.1)

fig=plt.figure()
ax=fig.add_subplot()
ax.hist(caso1,bins=100,density=True)
ax.plot(x,normal*12)
fig.savefig("histograma_0.5_100000.pdf")
plt.close(fig)

fig=plt.figure()
ax=fig.add_subplot()
ax.hist(caso2,bins=100,density=True)
ax.plot(x,normal*12)
fig.savefig("histograma_0.2_100000.pdf")
plt.close(fig)

fig=plt.figure()
ax=fig.add_subplot()
ax.hist(caso3,bins=100,density=True)
ax.plot(x,normal*12)
fig.savefig("histograma_0.01_100000.pdf")
plt.close(fig)

fig=plt.figure()
ax=fig.add_subplot()
ax.hist(caso4,bins=100,density=True)
ax.plot(x,normal*12)
fig.savefig("histograma_0.01_1000.pdf")
plt.close(fig)

fig=plt.figure()
ax=fig.add_subplot()
ax.hist(caso5,bins=100,density=True)
ax.plot(x,normal*12)
fig.savefig("histograma_0.1_100000.pdf")
plt.close(fig)