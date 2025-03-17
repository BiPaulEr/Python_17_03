liste_p = ["prenom1", "prenom2","prenom3", "prenom4"]
liste_n = ["nom1", "nom2","nom3"]

print(list(zip(liste_p, liste_n)))
#[('prenom1', 'nom1'), ('prenom2', 'nom2'), ('prenom3', 'nom3')]

for prenom, nom in zip(liste_p, liste_n):
    print("Bonjour ", prenom, nom)