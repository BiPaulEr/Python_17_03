liste = [5, 15, None, 10, 20] 

def nettoyer(liste):
    liste_new = []
    for element in liste:
        if not element is None:
            liste_new.append(element)
    return liste_new

def filtrer(liste):
    liste_new = []
    for element in liste:
        if element <= 10 and element >= 0:
            liste_new.append(element)
    return liste_new

def analyser(liste):
    return filtrer(nettoyer(liste))

liste_nettoye = nettoyer(liste)

liste_filtre = filtrer(liste_nettoye)

print(liste) #[5, 15, None, 10, 20]
print(liste_nettoye) #[5, 15, 10, 20]
print(liste_filtre) #[5, 10]

print(analyser(liste)) #[5, 10]
