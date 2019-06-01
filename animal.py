class Animal:
    def animal_sound(self,animal,sound):
       print( f"le {animal} fait {sound}.")
    def sound(self):
        raise NotImplementedError("la classe n'aps definit le son de l'animal")


class Chien(Animal):
    def sound(self):
        return {"Haw Haw"}

c=Chien()
print(c.sound())
