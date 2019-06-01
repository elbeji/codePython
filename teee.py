import numpy as np 
from numpy.random import rand
from numpy.linalg import solve, inv
print("Hello")
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a.transpose()
inv(a)
solve(a,b)
c=rand(3,3)
d=np.dot(a,c)
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
