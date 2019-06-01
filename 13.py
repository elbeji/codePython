class Humain:
    def __init__(self,nom,age):
        self.nom=nom
        self._age=age
    # property(getter , setter , deleter, helper)

    

    def _getage(self):
        return self._age

    def _setage(self,nage):
        if nage<0 :self._age=0
        else: self._age=nage
    age=property(_getage, _setage)


#programme principal
h1=Humain("Jojo",21)

print(h1.age)
h1.age=11
print(h1.age)

h1.nom="ALI"
nage=int(input("nouveau age pour Ali: "))
h1._age=nage


print("______________")
print(h1._age)
print("______________")
h1._setage(nage)
print(h1._age)


