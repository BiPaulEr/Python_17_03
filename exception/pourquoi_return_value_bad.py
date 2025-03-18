from random import randint

liste = []

def f1(liste):
    if randint(1, 100) > 50:
        return None
    else:
        liste.append(1)
        return liste

def f2(liste):
    if randint(1, 100) > 50:
        return None
    else:
        liste.append(2)
        return liste

def f3(liste):
    if randint(1, 100) > 50:
        return None
    else:
        liste.append(3)
        return liste

def f4(liste):
    if randint(1, 100) > 50:
        return None
    else:
        liste.append(4)
        return liste
    
liste2 = f1(liste)
if liste2:
    liste3 = f2(liste2)
    if liste3:
        liste4 = f3(liste3)
        if liste4:
            liste5 = f4(liste4) #errue
            print(liste5)