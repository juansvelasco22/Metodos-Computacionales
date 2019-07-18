import numpy as np
import matplotlib.pylab as plt

#Punto 1
#a. Distribucion Uniforme
uniforme=np.random.uniform(-10,10,1000)
gaus=np.random.normal(17,5,1000)
fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(131)

ax1.hist(uniforme, bins=20, label="Datos")
ax1.set_xlabel("Valores")
ax1.set_ylabel("Repeticiones")

ax1.legend()

#b.Distribucion Gaussiana
gaus=np.random.normal(17,5,1000)
fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(131)

ax1.hist(gaus, bins=20, label="Datos")
ax1.set_xlabel("Valores")
ax1.set_ylabel("Repeticiones")

ax1.legend()
fig.savefig("gausiana.pdf")

#Punto 2
#a. Cuadrado
cuadrado=np.random.uniform(0,30.5,1000)
linea=np.linspace(0,30.5,1000)
plt.scatter(cuadrado,linea, label="Datos")
plt.xlabel("Lado x")
plt.ylabel("Lado y")
plt.legend()
plt.savefig("cuadrado.pdf")

#b.Circulo
theta=np.random.uniform(0,2*np.pi,1000)
r=np.random.uniform(0,23,1000)
x=r*np.cos(theta)
y=r*np.sin(theta)

plt.scatter(x,y, label="Datos")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Distribucion en un circulo de radio 23")
plt.axis("equal")
plt.legend()
plt.savefig("circulo.pdf")


#Punto 4
inicio=np.array([[cuadrado],[linea]])
x=np.zeros(1000)
y=np.zeros(1000)
for i in range(1000):
    for j in range(100):
        pasos=np.random.normal(0,0.25,(2,100))
        x[i]=cuadrado[i]+pasos
        y[i]=liena[i]+pasos
