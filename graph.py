import numpy as np
import matplotlib.pyplot as plt

archivo=np.loadtxt('laminas.txt')

laminas=archivo[:,0]
repetidas=archivo[:,1]
dominio=np.arange(len(laminas))
plt.plot(dominio,laminas)
plt.plot(dominio,repetidas)
plt.savefig('grafica.png')
