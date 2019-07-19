import numpy as np
import matplotlib.pylab as plt

#Importar los datos
euler1=np.genfromtxt("e_0.0001.dat",delimiter=" ")
euler2=np.genfromtxt("e_0.00001.dat",delimiter=" ")
euler3=np.genfromtxt("e_0.000001.dat",delimiter=" ")
LF1=np.genfromtxt("LP_0.0001.dat",delimiter=" ")
LF2=np.genfromtxt("LP_0.00001.dat",delimiter=" ")
LF3=np.genfromtxt("LP_0.000001.dat",delimiter=" ")

#organizar los datos en variables para facilitar su uso
ex1=euler1[:,0]
ey1=euler1[:,1]
evx1=euler1[:,2]
evy1=euler1[:,3]
er1=euler1[:,4]
et1=euler1[:,5]

ex2=euler2[:,0]
ey2=euler2[:,1]
evx2=euler2[:,2]
evy2=euler2[:,3]
er2=euler2[:,4]
et2=euler2[:,5]

ex3=euler3[:,0]
ey3=euler3[:,1]
evx3=euler3[:,2]
evy3=euler3[:,3]
er3=euler3[:,4]
et3=euler3[:,5]

lx1=LF1[:,0]
ly1=LF1[:,1]
lvx1=LF1[:,2]
lvy1=LF1[:,3]
lr1=LF1[:,4]
lt1=LF1[:,5]

lx2=LF2[:,0]
ly2=LF2[:,1]
lvx2=LF2[:,2]
lvy2=LF2[:,3]
lr2=LF2[:,4]
lt2=LF2[:,5]

lx3=LF3[:,0]
ly3=LF3[:,1]
lvx3=LF3[:,2]
lvy3=LF3[:,3]
lr3=LF3[:,4]
lt3=LF3[:,5]

em1=5.972*(10**24) *er1*2*np.pi
em2=5.972*(10**24) *er2*2*np.pi
em3=5.972*(10**24) *er3*2*np.pi

G=6.674*(10**(-29))
Msol=1.989*(10**(30))
Mtierra=5.972*(10**24)

eE1=(1/2)*Mtierra*((evx1+evy1)**2)+(-G*(Msol*Mtierra)/er1)
eE2=(1/2)*Mtierra*((evx2+evy2)**2)+(-G*(Msol*Mtierra)/er2)
eE3=(1/2)*Mtierra*((evx3+evy3)**2)+(-G*(Msol*Mtierra)/er3)

lm1=5.972*(10**24) *lr1*2*np.pi
lm2=5.972*(10**24) *lr2*2*np.pi
lm3=5.972*(10**24) *lr3*2*np.pi

lE1=(1/2)*Mtierra*((lvx1+lvy1)**2)+(-G*(Msol*Mtierra)/lr1)
lE2=(1/2)*Mtierra*((lvx2+lvy2)**2)+(-G*(Msol*Mtierra)/lr2)
lE3=(1/2)*Mtierra*((lvx3+lvy3)**2)+(-G*(Msol*Mtierra)/lr3)

#Grafica de las posiciones X vs Y
pos=plt.figure(figsize=(15,5))
ax1=pos.add_subplot(231)
ax2=pos.add_subplot(232)
ax3=pos.add_subplot(233)
ax4=pos.add_subplot(234)
ax5=pos.add_subplot(235)
ax6=pos.add_subplot(236)

ax1.plot(ex1,ey1, label="Orbitas")
ax1.set_ylabel("Distancia Y Euler")
ax1.set_title("dt=0.0001")
ax1.axis("equal")

ax2.plot(ex2,ey2)
ax2.set_title("dt=0.00001")
ax2.axis("equal")

ax3.plot(ex3,ey3)
ax3.set_title("dt=0.000001")
ax3.axis("equal")

ax4.plot(lx1,ly1)
ax4.set_xlabel("Distancia X")
ax4.set_ylabel("Distancia Y L-F")
ax4.axis("equal")

ax5.plot(lx2,ly2)
ax5.set_xlabel("Distancia X")
ax5.axis("equal")

ax6.plot(lx3,ly3)
ax6.set_xlabel("Distancia X")
ax6.axis("equal")
pos.legend()
pos.savefig("XY_met_dt.pdf")
plt.close(pos)


#Grafica de las Velocidades X vs Y
vel=plt.figure(figsize=(15,5))
ax1=vel.add_subplot(231)
ax2=vel.add_subplot(232)
ax3=vel.add_subplot(233)
ax4=vel.add_subplot(234)
ax5=vel.add_subplot(235)
ax6=vel.add_subplot(236)

ax1.plot(evx1,evy1, label="Orbitas")
ax1.set_ylabel("Velocidad Y Euler")
ax1.set_title("dt=0.0001")
ax1.axis("equal")

ax2.plot(evx2,evy2)
ax2.set_title("dt=0.00001")
ax2.axis("equal")

ax3.plot(evx3,evy3)
ax3.set_title("dt=0.000001")
ax3.axis("equal")

ax4.plot(lvx1,lvy1)
ax4.set_xlabel("Velocidad X")
ax4.set_ylabel("Velocidad Y L-F")
ax4.axis("equal")

ax5.plot(lvx2,lvy2)
ax5.set_xlabel("Velocidad X")
ax5.axis("equal")

ax6.plot(lvx3,lvy3)
ax6.set_xlabel("Velocidad X")
ax6.axis("equal")
vel.legend()
vel.savefig("VxVy_met_dt.pdf")
plt.close(vel)

#Grafica del momento angular en funcion del tiempo
mom=plt.figure(figsize=(15,5))
ax1=mom.add_subplot(231)
ax2=mom.add_subplot(232)
ax3=mom.add_subplot(233)
ax4=mom.add_subplot(234)
ax5=mom.add_subplot(235)
ax6=mom.add_subplot(236)

ax1.plot(et1,em1, label="Valores")
ax1.set_ylabel("Momento angular Euler")
ax1.set_title("dt=0.0001")

ax2.plot(et2,em2)
ax2.set_title("dt=0.00001")

ax3.plot(et3,em3)
ax3.set_title("dt=0.000001")

ax4.plot(lt1,lm1)
ax4.set_xlabel("Tiempo")
ax4.set_ylabel("Momento angular L-F")

ax5.plot(lt2,lm2)
ax5.set_xlabel("Tiempo")

ax6.plot(lt3,lm3)
ax6.set_xlabel("Tiempo")
mom.legend()
mom.savefig("Mome_met_dt.pdf")
plt.close(mom)

#Grafica de las Energia en funcion del tiempo
ene=plt.figure(figsize=(15,5))
ax1=ene.add_subplot(231)
ax2=ene.add_subplot(232)
ax3=ene.add_subplot(233)
ax4=ene.add_subplot(234)
ax5=ene.add_subplot(235)
ax6=ene.add_subplot(236)

ax1.plot(et1,eE1, label="Valores")
ax1.set_ylabel("Energia Euler")
ax1.set_title("dt=0.0001")

ax2.plot(et2,eE2)
ax2.set_title("dt=0.00001")

ax3.plot(et3,eE3)
ax3.set_title("dt=0.000001")

ax4.plot(lt1,lE1)
ax4.set_xlabel("Tiempo")
ax4.set_ylabel("Energia L-F")

ax5.plot(lt2,lE2)
ax5.set_xlabel("Tiempo")

ax6.plot(lt3,lE3)
ax6.set_xlabel("Tiempo")
ene.legend()
ene.savefig("Ener_met_dt.pdf")
plt.close(ene)