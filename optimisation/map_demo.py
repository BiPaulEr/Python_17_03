prenoms = ["prenom"] * 10

prenoms_majuscule = list(map(lambda chaine: chaine.capitalize(), prenoms))
prenoms_minuscule = list(map(lambda chaine: chaine.lower(), prenoms))
prenoms_test = list(map(lambda chaine: None, prenoms))
"""
for index, prenom in enumerate(prenoms):
    prenoms[index] = titre(prenom)"
"""

print(prenoms)
print(prenoms_majuscule)
print(prenoms_test)