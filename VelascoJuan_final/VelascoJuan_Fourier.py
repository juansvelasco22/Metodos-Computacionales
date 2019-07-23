
import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft
import scipy.fftpack

n = 1280 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 320 ) #320 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)
amp = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t ) + np.random.random(n)

# SU FILTRO
trans=np.fft.fft(amp)
freq=np.fft.fftfreq(1280,dt)

filtrado=[]
for i in range(1280):
    if(abs(freq[i])<1000):
        filtrado.append(freq[i])
    else:
        freq[i]=0
        filtrado.append(freq[i])
        
inversa=np.fft.ifft(filtrado)

# SU GRAFICA

fig=plt.figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

ax1.plot(amp, label="Datos")
ax1.set_xlabel("Distancia")
ax1.set_ylabel("Amplitud")
ax1.set_title("Datos originales")
ax2.plot(inversa,label="Datos")
ax2.set_xlabel("Distancia")
ax2.set_title("Datos depues del filtro")

ax1.legend()
ax2.legend()

fig.savefig("filtro.pdf")
plt.close(fig)

