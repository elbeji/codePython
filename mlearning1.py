import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([[1980],[1983],[1984],[1990],[1994]])
y = np.array([[1500],[1580],[1850],[3520],[4000]])
plt.scatter(x ,y)
plt.title("Used Cars Prices", fontsize=24)
plt.xlabel("X axes", fontsize=14)
plt.ylabel("Y axes", fontsize=14)
plt.grid(True)

model = LinearRegression()
model.fit(x,y)
h=model.predict([1987])
print(h)




plt.show()
