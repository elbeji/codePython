a=input("entrer votre age :")
b=5
try :
    age=int(b/a)
#except: ZeroDivisionError 
    print("age doit etre # 0")
except:
    print("erreur dans la saisie de l'age")
else:
    print("votre age est ",age)
finally:
    print("fin du programme")
