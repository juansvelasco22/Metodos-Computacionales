import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("Canal_ionico.txt")

x=np.random.uniform()
y=np.random.uniform()

valx=np.array([])
valy=np.array([])

def MH(pasos,sigma):
    cx=np.random.uniform()
    cy=np.random.uniform()
    valx=np.append(valx,cx)
    valy=np.append(valy,cy)
    
    for i in range(pasos):
        
        alpha=(cx)/(x)
        
        if(alpha>=1):
            valx=np.append(valx,cx)
            valy=np.append(valy,cy)
            
            beta=np.random.uniform()
            if(beta<alpha):
                valx=np.append(valx,cx)
                valy=np.append(valy,cy)
            else:
                valx=np.append(valx,valx[i])
                valy=np.append(valy,valy[i])
    return valx, valy


fig=plt.figure()
ax1=fig.add_subplot(121)

ax1.plot(valx,valy)
ax1.scatter(datos[:,0],datos[:,1])

fig.davefig("Canal.png")
plt.close(fig)