chaine = "Bonjour Python"

for index in range(len(chaine) -1 , -1, -1 ):
    print(chaine[index])

"""
for letter in reversed(chaine):
    print(letter)
"""

liste = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for index, valeur in enumerate(liste):
    print(index, " - > ", valeur)