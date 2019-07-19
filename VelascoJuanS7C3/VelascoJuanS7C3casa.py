import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("resorte.dat",delimiter=" ")

t=datos[:,0]
x=datos[:,1]

def modelo(a,gamma,omega):
    xt=a*np.exp(-gamma*t)*np.cos(omega*t)
    return xt

def LK(yobs,ymod):
    chi_2=np.sum((yobs-ymod)**2)
    L=np.exp(-(1.0/2.0)*chi_2)
    return L

aini=7.5
gammaini=0.6
omegaini=18.2
iteraciones=100000

def Bayesiana(numpasos,sigma):
    
    a=np.array([])
    gamma=np.array([])
    omega=np.array([])
    L=np.array([])
    
    a=np.append(a,aini)
    gamma=np.append(gamma,gammaini)
    omega=np.append(omega,omegaini)
    L=np.append(L,LK(x,modelo(aini,gammaini,omegaini)))
    
    
    for i in range(numpasos):
        
        anuevo=np.random.normal(a[i],sigma)
        gammanuevo=np.random.normal(gamma[i],sigma)
        omeganuevo=np.random.normal(omega[i],sigma)
        L_nuevo=LK(x,modelo(anuevo,gammanuevo,omeganuevo))
        L_viejo=LK(x,modelo(a[i],gamma[i],omega[i]))
        
        alpha=(L_nuevo/L_viejo)
        
        if(alpha>=1):
            a=np.append(a,anuevo)
            gamma=np.append(gamma,gammanuevo)
            omega=np.append(omega,omeganuevo)
            L=np.append(L,L_nuevo)
        else:
            beta=np.random.uniform()
            
            if(beta<alpha):
                a=np.append(a,anuevo)
                gamma=np.append(gamma,gammanuevo)
                omega=np.append(omega,omeganuevo)
                L=np.append(L,L_nuevo)
            else:
                a=np.append(a,a[i])
                gamma=np.append(gamma,gamma[i])
                omega=np.append(omega,omega[i])
                L=np.append(L,L_viejo)
                
    return a,gamma,omega,L

r=Bayesiana(iteraciones, 5)

a=r[0]
g=r[1]
o=r[2]
ll=r[3]

max=np.argmax(ll)
mejorL=ll[max]
mejora=a[max]
mejorgamma=g[max]
mejoromega=o[max]

print("Los mejores parametros son: a= ",mejora, " gamma= ",mejorgamma, " omega= ",mejoromega)

best_fit=modelo(mejora,mejorgamma,mejoromega)

fig=plt.figure(figsize=(20,5))
ax1=fig.add_subplot(131)
ax2=fig.add_subplot(132)

ax1.plot(t,x,c="C3",label="datos")
ax1.plot(t,best_fit, label="Ajuste")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Posicion")
ax1.set_title("Datos graficados como una linea")
ax1.legend()

ax2.scatter(t,x,c="C3",label="datos")
ax2.plot(t,best_fit, label="Ajuste")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("Posicion")
ax2.set_title("Datos graficados como puntos")
ax2.legend()

fig.savefig("Resorte.pdf")
plt.close(fig)