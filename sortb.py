import os
def sortb(arr):
    while True :
        corrected = False
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                corrected = True
        if not corrected :
            return arr
t=[k for k in range(1,10) input()] 
print(sortb(t))