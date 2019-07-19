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

L_max=np.argmax(ll)

def mejores():
    valor=0
    for i in range(len(ll)):
        if(ll[i]==L_max):
            valor=i
    return valor