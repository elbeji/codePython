import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(0)
df = pd.DataFrame(randn(4,4),['A','B','C','X'],['D','E','F','Y'])
print(df)


df2= pd.DataFrame(randn(6,8),['Lundi','Mardi','Mercredi','Jeud','Vendredi','Samedi',],
                  ['8-9','9-10','10-11','11-12','14-15','15-16','16-17','17-18'])

