n=int(input('Nombre de notes a saisir :'))
s=0
for i in range(n):
    s+=float(input('saisir la note '))

moy=s/n
print('La moyenne est ',moy)
if (moy>10):
    print('ADMIS')
else:
    print('Refuse')