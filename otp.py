import math , random
digits='0123456789abcdefghijklmnopqrstuvwxyz!@#$%&*ABCDEFGHIJKLOPMNVXZQWERTYUS()'
otp=''
l=[]
f=open('a:\pwd.txt','a')
for k in range(1,11):
    for  i in range(1,9):
        otp+=digits[math.floor(random.random()*len(digits))]
    print(otp)
    otp+='\n'
    f.write(otp)
    otp=''
f.close()

    
