

class Humain:
    humain_cree=0#attribut de classe
    def __init__(self,cprenom,cage):#constructeur
        self.prenom=cprenom
        self.age=cage
        Humain.humain_cree +=1

    def parler(self , message):#methode de classe
        print("{} a dit :{}".format(self.prenom , message))
        







print("lancement de programme")
h1 = Humain("jojo",1)#instanciation de la classe
h1.age=17#acces et modification d un attribut

#print("prenom de h1 :{}".format(h1.prenom))
h2 = Humain("dodo",2)
h3=Humain("mmm",21)
print("prenom de h1 :{}".format(h1.prenom))
print("age    de h1 :{}".format(h1.age))
print("prenom de h2 :{}".format(h2.prenom))
print("age    de h1 :{}".format(h2.age))

print("Nombre des humain est :{}".format(Humain.humain_cree))
h1.parler("Bonjour ")#appel a la methode de classe
