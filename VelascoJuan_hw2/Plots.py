import numpy as np
import matplotlib.pylab as plt

euler1=np.genfromtxt("euler_0.0001.dat",delimiter=" ")
euler2=np.genfromtxt("euler_0.00001.dat",delimiter=" ")
euler3=np.genfromtxt("euler_0.000001.dat",delimiter=" ")

x=euler1[:,0]
y=euler1[:,1]
vx=euler1[:,2]
vy=euler1[:,3]
r=euler1[:,4]