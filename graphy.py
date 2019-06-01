import os
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-4*np.pi, 4*np.pi)
y=np.cos(x)
plt.plot(x,y)
plt.legend()
plt.xlabel('X')
plt.ylabel('Y=Cos(x)')
plt.show()
