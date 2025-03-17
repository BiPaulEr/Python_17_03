liste  = [1, -1, 2, -2, 3, -3]

for num in liste:
    if num < 0:
        continue
    print(num)

mots_de_passe = ["12345678", "password123", "abc123", "pythoniscool"]

for mdp in mots_de_passe:
    print(mdp)
    if len(mdp) < 8:
        print("Mot Faible Trouve !! ", mdp)
        break

elements = ['pomme', 'banane', 'cerise', 'date', 'banane', 'baie']
elements_deja_vue = []
for element in elements:
    if not element in elements_deja_vue:
        print(element)
        elements_deja_vue.append(element)
    else:
        print(element, " est en double ")
        break
