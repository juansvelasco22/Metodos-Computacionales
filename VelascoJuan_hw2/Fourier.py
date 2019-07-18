import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq
from scipy import fftpack
from matplotlib.colors import LogNorm


#Importar los archivos de las fotografias
cara1=plt.imread("cara_02_grisesMF.png")
cara2=plt.imread("cara_03_grisesMF.png")


#Usando los paquetes de Numpy calculamos la transformada de Fourier

Fcara1=fftpack.fft2(cara1)
Fcara2=fftpack.fft2(cara2)

#Graficas de los espectros de Fourier de las dos imagenes
plt.imshow(abs(Fcara1), norm=LogNorm(vmin=1))
plt.colorbar()
plt.imshow(np.abs(Fcara2), norm=LogNorm(vmin=1))
plt.colorbar()




#Tomar de la cara 1 las frecuencias altas
filas1, columnas1 =Fcara1.shape
freq1=Fcara1
freq1[int(filas1*0.05):int(filas1*(1-0.05))] = 0
freq1[:, int(columnas1*0.05):int(columnas1*(1-0.05))] = 0
plt.imshow(abs(freq1), norm=LogNorm(vmin=1))
plt.colorbar()

filas2, columnas2 =Fcara2.shape
freq2=Fcara2.copy()
freq2[int(filas2*0.05):int(filas2*(1-0.05))] = 0
freq2[:,int(columnas2*0.05):int(columnas2*(1-0.05))] = 0
Filtro = (Fcara2-freq2)
plt.imshow(abs(Filtro), norm=LogNorm(vmin=1))
plt.colorbar()

Nueva=(Filtro+freq1)
plt.imshow(abs(Nueva), norm=LogNorm(vmin=1))
plt.colorbar()

Inversa=fftpack.ifft2(Nueva)
plt.imshow(abs(Inversa),plt.cm.gray)