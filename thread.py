import time
import threading 

verou=threading.RLock()
def f1():
    i=0
    while i<3 :
        with verou:
            ch="ABC"
            for c in ch:
                print(c)
                time.sleep(1.3)
        i+=1
def f2():
    i=0
    while i<3:
        print("f2 VVVVVVV")
        time.sleep(1.3)
        i+=1
print("Execution sequentielle")
f1()
f2()
print("----------------------")

print(" execution asynchrone ")

th1=threading.Thread(target =f1)
th2=threading.Thread(target =f2)

th1.start()
th2.start()
th1.join()
th2.join()
