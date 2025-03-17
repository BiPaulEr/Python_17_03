liste = ["prenom1", "prenom2","prenom3"]

for index in range(0, len(liste), 1):
    print(index)
    liste[index] = liste[index].upper()
    print(liste)

print(list(enumerate(liste)))
#[(0, 'PRENOM1'), (1, 'PRENOM2'), (2, 'PRENOM3')]

for index, valeur in enumerate(liste):
    print(index," ", valeur)
    liste[index] = valeur.lower()

print(liste) #['prenom1', 'prenom2', 'prenom3']