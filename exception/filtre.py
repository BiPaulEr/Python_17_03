from random import randint

liste = []

def f1(liste):
    if randint(1, 100) > 50:
        raise Exception("f1")
    else:
        liste.append(1)
        return liste

def f2(liste):
    if randint(1, 100) > 50:
        raise Exception("f2")
    else:
        liste.append(2)
        return liste

def f3(liste):
    if randint(1, 100) > 50:
        raise Exception("f3")
    else:
        liste.append(3)
        return liste

def f4(liste):
    if randint(1, 100) > 50:
        raise Exception("f4")
    else:
        liste.append(4)
        return liste
try:
    liste2 = f1(liste)
    liste3 = f2(liste2)
    liste4 = f3(liste3)
    liste5 = f4(liste4) #errue
    print(liste5)
except Exception as e:
    print(e)
else:
    print("pas d'erreur")
finally:
    print("Tout le temps execute")