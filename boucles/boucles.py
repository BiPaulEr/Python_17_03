liste = ["prenom1", "prenom2","prenom3","prenom4"]

"""
liste[0] = liste[0].upper()
liste[1] = liste[1].upper()
liste[2] = liste[2].upper()
liste[3] = liste[3].upper()"
"""
for index in [0, 1, 2, 3]:
    print(index)
    liste[index] = liste[index].upper()
    print(liste)

for prenom in liste:
    print(prenom)

print(liste)