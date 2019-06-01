class Contact:
    def __init__(self, nom,age):
        self.nom=nom
        self._age=age
    def get_age(self):
        return self._age
    def set_age(self,new_age):
        if new_age>0 :
            self._age=new_age
        else:
            self._age=0
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,newage):
        if newage>0:
            self._age=newage
        else:
            print("age incorrect")
            self._age=0

c0=Contact("Omi",62)
c1=Contact("Mourad",42)
c2=Contact("Mehdi",2)
#print(c1.get_age())
#print(c2.get_age())
c1.set_age(34)
#print(c1.get_age())
c1.set_age(-3)
#print(c1.get_age())
print(c0.age)
c2.age=-99
print(c2.age)