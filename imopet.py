#import numpy as np   
#import re
class User:
    def __init__(self, name, age,email):
        self.name=name
        self.age=age
        self.email=email
        self._secret="Mehdi aime le chocolat"
        self.__friend="Ziko Rahma Anas Ghazal"
    def identity(self):
        return f"Name: {self.name}   Age:{self.age}"


fuser=User("Mourad",42,"elbeji@gmail.com")
suser=User("Mehdi",2,"mehdibeji@gmail.com")

print(fuser.identity())
print(suser.identity())




