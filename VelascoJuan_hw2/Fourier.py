import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq
from scipy import fftpack


#Importar los archivos de las fotografias
cara1=plt.imread("cara_02_grisesMF.png")
cara2=plt.imread("cara_03_grisesMF.png")


#Usando los paquetes de Numpy calculamos la transformada de Fourier

fouriercara1=fftpack.fft2(cara1).real
fouriercara2=fftpack.fft2(cara2).real

frec=np.fft.fftfreq(len(fouriercara1),1)
frecc=np.fft.fftfreq(245,1)
freq2=np.fft.fftshift(frec)


plt.plot(frec,fouriercara1)
plt.xlabel('Frecuencias')
plt.ylabel('Amplitud')


plt.plot(frec,fouriercara2)
plt.xlabel('Frecuencias')
plt.ylabel('Amplitud')


fouriercara1[abs(frec) > 0.1] = 0
fouriercara2[abs(frec) < 0.1] = 0