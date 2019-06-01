l=['Naima','Moncef','ahmed','slim','mourad','Houda','Mehdi']
s='mourad'

for i in range(0,12):
    for j in range(i):
        print('%-4d ' %(i+j-1),end=' ')
    print()

start=2
end=100
for i in range(start,end+1):
    if i>1 :
        for j in range(2,i):
            if (i %j) ==0 : 
                break
        else :
            print(i, ' -- ',i+2,' -- ' ,i+6,' -- ',i+8)
