prenoms = ["prenom", "pol", "okokokokokokokoko", "cal"]

prenoms_true = list(filter(lambda chaine: True, prenoms))
print(prenoms_true) #['prenom', 'pol', 'okokokokokokokoko', 'cal']

prenoms_false = list(filter(lambda chaine: False, prenoms))
print(prenoms_false) #[]

prenoms_filtre = list(filter(lambda chaine: len(chaine) < 4, prenoms))
print(prenoms_filtre) #['pol', 'cal']

prenoms_filtre_long = list(filter(lambda chaine: len(chaine) > 4, prenoms))
print(prenoms_filtre_long) #['prenom', 'okokokokokokokoko']