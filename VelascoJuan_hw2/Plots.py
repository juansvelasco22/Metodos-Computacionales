import numpy as np
import matplotlib.pylab as plt

#Importar los datos
datos1=np.genfromtxt("e_0.005.dat",delimiter=" ")
datos2=np.genfromtxt("e_0.001.dat",delimiter=" ")
datos3=np.genfromtxt("e_0.0001.dat",delimiter=" ")

#organizar los datos en variables para facilitar su uso
x1=datos1[:,0]
y1=datos1[:,1]
vx1=datos1[:,2]
vy1=datos1[:,3]
r1=datos1[:,4]
t1=datos1[:,5]

x2=datos2[:,0]
y2=datos2[:,1]
vx2=datos2[:,2]
vy2=datos2[:,3]
r2=datos2[:,4]
t2=datos2[:,5]

x3=datos3[:,0]
y3=datos3[:,1]
vx3=datos3[:,2]
vy3=datos3[:,3]
r3=datos3[:,4]
t3=datos3[:,5]

m1=5.972*(10**24) *r1*2*np.pi
m2=5.972*(10**24) *r2*2*np.pi
m3=5.972*(10**24) *r3*2*np.pi

G=6.674*(10**(-29))
Msol=1.989*(10**(30))
Mtierra=5.972*(10**24)

E1=(1/2)*Mtierra*((vx1+vy1)**2)+(-G*(Msol*Mtierra)/r1)
E2=(1/2)*Mtierra*((vx2+vy2)**2)+(-G*(Msol*Mtierra)/r2)
E3=(1/2)*Mtierra*((vx3+vy3)**2)+(-G*(Msol*Mtierra)/r3)


#Grafica de las posiciones X vs Y
pos=plt.figure(figsize=(15,5))
ax1=pos.add_subplot(131)
ax2=pos.add_subplot(132)
ax3=pos.add_subplot(133)

ax1.plot(x1,y1, label="Orbitas")
ax1.set_xlabel("Distancia X")
ax1.set_ylabel("Distancia Y")
ax1.set_title("dt=0.005")
ax1.axis("equal")

ax2.plot(x2,y2)
ax2.set_xlabel("Distancia X")
ax2.set_title("dt=0.001")
ax2.axis("equal")

ax3.plot(x3,y3)
ax3.set_xlabel("Distancia X")
ax3.set_title("dt=0.0001")
ax3.axis("equal")

pos.legend()


#Grafica de las velocidades Vx vs Vy
vel=plt.figure(figsize=(15,5))
ax1=vel.add_subplot(131)
ax2=vel.add_subplot(132)
ax3=vel.add_subplot(133)

ax1.plot(vx1,vy1, label="Orbitas")
ax1.set_xlabel("Velocidad X")
ax1.set_ylabel("Velocidad Y")
ax1.set_title("dt=0.005")
ax1.axis("equal")

ax2.plot(vx2,vy2)
ax2.set_xlabel("Velocidad X")

ax2.set_title("dt=0.001")
ax2.axis("equal")

ax3.plot(vx3,vy3)
ax3.set_xlabel("Velocidad X")

ax3.set_title("dt=0.0001")
ax3.axis("equal")

vel.legend()

#Grafica del momento angular en funcion del tiempo

mom=plt.figure(figsize=(15,5))
ax1=mom.add_subplot(131)
ax2=mom.add_subplot(132)
ax3=mom.add_subplot(133)

ax1.plot(t1,m1,label="Valores")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Momento angular")
ax1.set_title("dt=0.005")


ax2.plot(t2,m2)
ax2.set_xlabel("Tiempo")
ax2.set_title("dt=0.001")


ax3.plot(t3,m3)
ax3.set_xlabel("Tiempo")
ax3.set_title("dt=0.0001")


mom.legend()


#Grafica de la energia en funcion del tiempo
ene=plt.figure(figsize=(15,5))
ax1=ene.add_subplot(131)
ax2=ene.add_subplot(132)
ax3=ene.add_subplot(133)

ax1.plot(t1,E1,label="Energia")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Energia")
ax1.set_title("dt=0.005")


ax2.plot(t2,E2)
ax2.set_xlabel("Tiempo")
ax2.set_title("dt=0.001")


ax3.plot(t3,E3)
ax3.set_xlabel("Tiempo")
ax3.set_title("dt=0.0001")


ene.legend()