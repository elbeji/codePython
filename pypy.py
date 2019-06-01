import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.arange(-3,3,0.5)
y=x**2
z=np.sin(x)
w=np.exp(-x**2)
plt.plot(x,y,x,z,x,w,x,x)
plt.show()