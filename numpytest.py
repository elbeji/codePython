import numpy as np
import sys
import time
size =100000
a = np.array([(1,2,3),(4,5,6)])
L1= range(size)
L2=range(size)
a1 = np.arange(size)
a2 = np.arange(size)
start=time.time()
print("time 1",start)
result= [(x,y) for x,y in zip(L1,L2)]
print("result 1",result)
start=time.time()
result =a1+a2
print("time 2",start)
print("result 2 ",result)
print((time.time()-start)*1000)
