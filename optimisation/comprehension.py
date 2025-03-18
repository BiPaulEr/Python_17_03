prenoms = ["prenom", None, "pol", "okokokokokokokoko", "cal"]
prenoms_filter = list(filter(lambda chaine: chaine is not None, prenoms))
print(prenoms_filter)
prenoms_majuscule = list(map(lambda chaine: chaine.capitalize(), prenoms_filter))
print(prenoms_majuscule)

#ok = list(map(lambda chaine: chaine.capitalize(), filter(lambda chaine: chaine is not None, prenoms)))

prenom_majuscule_c = [prnom.capitalize() for prnom in  prenoms if prnom is not None]
print(prenom_majuscule_c) #['Prenom', 'Pol', 'Okokokokokokokoko', 'Cal']