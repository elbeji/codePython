#methode de classe
class Humain:
    lieu="Terre"
    def __init__(self,nom,age):#constructeur
        self.nom=nom
        self.age=age
    def parler(self,message):#methode d'instance
        print("{} a dit :{}".format(self.nom, message))
    def changelieu(cls,lieu):# methode de classe
        Humain.lieu=lieu
    changelieu = classmethod(changelieu)
    def defin():
        print(" blaaaaaaaaaaaaa ")
    defin = staticmethod(defin)

#programme principal
h1=Humain("bob",24)
h1.parler(" bonjour ")
#methode d'instancde ne fonctionne que sur des
# objets de la classe
Humain.changelieu("Mars")
#methode de classe elle travaille sur la classe
# elle meme
print("planete actuelle :{}".format(Humain.lieu))

Humain.defin()
