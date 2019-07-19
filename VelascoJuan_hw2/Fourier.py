import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
from scipy import fftpack
from matplotlib.colors import LogNorm


#Importar los archivos de las fotografias
cara2=plt.imread("cara_02_grisesMF.png")
cara1=plt.imread("cara_03_grisesMF.png")


#Usando los paquetes de Numpy calculamos la transformada de Fourier

Fcara1=fftpack.fft2(cara1)
Fcara2=fftpack.fft2(cara2)

#Graficas de los espectros de Fourier de las dos imagenes
fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.imshow(abs(Fcara1), norm=LogNorm(vmin=1))
ax1.set_title("Espectro de Fourier de cara 1")

ax2.imshow(abs(Fcara2), norm=LogNorm(vmin=1))
ax2.set_title("Espectro de Fourier de cara 2")
fig.colorbar(plt.cm.ScalarMappable())
fig.savefig("Espectros_fourier.pdf")
plt.close(fig)



#Tomar de la cara 1 las frecuencias altas
filas1, columnas1 =Fcara1.shape
freq1=Fcara1
freq1[int(filas1*0.05):int(filas1*(1-0.05))] = 0
freq1[:, int(columnas1*0.05):int(columnas1*(1-0.05))] = 0

#Tomar las frecuencias bajas de la cara 2
filas2, columnas2 =Fcara2.shape
freq2=Fcara2.copy()
freq2[int(filas2*0.05):int(filas2*(1-0.05))] = 0
freq2[:,int(columnas2*0.05):int(columnas2*(1-0.05))] = 0

#Graficar los filtros de las caras
Filtro = (Fcara2-freq2)
fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.imshow(abs(freq1), norm=LogNorm(vmin=1))
ax1.set_title("Filtro de frecuencias altas")
ax2.imshow(abs(Filtro), norm=LogNorm(vmin=1))
ax2.set_title("Filtro de frecuencias bajas")
fig.colorbar(plt.cm.ScalarMappable())
fig.savefig("Filtros.pdf")
plt.close(fig)

#Generar el nuevo espectro que corresponde a la suma de los dos filtros
Nueva=(Filtro+freq1)
plt.imshow(abs(Nueva), norm=LogNorm(vmin=1))
plt.title("Espectro con la suma de los filtros")
plt.colorbar()
plt.savefig("Espectro_nuevo.pdf")
plt.close()


#Encontrar la transformada inversa para volver a obtener la imagen hibrida
Inversa=fftpack.ifft2(Nueva)
plt.imshow(abs(Inversa),plt.cm.gray)
plt.title("Cara Hibrida")
plt.savefig("Cara_Hibrida.pdf")
plt.close()