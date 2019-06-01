import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

xyz_web={'State':['Tunis','Beja','Gafsa','Sousse'],'Pop':[2500,350,650,700],'Succes':[54,35,23,56]}

df=pd.DataFrame(xyz_web)
df.set_index('State',inplace=True)

df.plot()
plt.show()
