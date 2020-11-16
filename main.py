import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,0.45,step=0.2*1e-3)
mu=0.45/2
sigma=0.05
f0=500
E=1/(sigma*np.sqrt(2*np.pi))*np.exp(-((x-mu))**2/(2*sigma**2))*(np.sin(f0*x)+np.sin(f0*2*x)+np.sin(f0/2*x)+np.sin(10*f0*x)+np.sin(f0*5*x))
plt.figure(figsize=(12,5))
plt.plot(x,E,'-k')
plt.grid(True)
plt.xlabel('x,m')
plt.ylabel('E(t)')
plt.show()
F=np.fft.fft(E)
freq = np.fft.fftfreq(x.shape[-1])
ar=np.sqrt((F.real)**2+(F.imag)**2)
plt.figure(figsize=(12,5))
plt.plot(freq, ar/np.max(ar),'r-')
plt.xlabel('f')
plt.ylabel('A')
plt.grid(True)
plt.show()
