def conversion_celsis_to_farenheit(degree_C):
    degree_F = degree_C * 9/5 + 32
    return degree_F

degree = 20
degree_Fa = conversion_celsis_to_farenheit(degree)
print(degree, " -> ", degree_Fa)

liste_Celsius = [12, 20, 0, -2, 23, 7]

def convertion_liste_to_farenheit(liste_c):
    for index, valeur in enumerate(liste_c):
        liste_c[index] = conversion_celsis_to_farenheit(valeur)

convertion_liste_to_farenheit(liste_Celsius)
print(liste_Celsius) #[53.6, 68.0, 32.0, 28.4, 73.4, 44.6]



liste_Celsius = [12, 20, 0, -2, 23, 7]
def new_convertion_liste_to_farenheit(liste_c):
    new_liste_f = []
    for valeur in liste_c:
        new_liste_f.append(conversion_celsis_to_farenheit(valeur))
    return new_liste_f

new_liste_f = new_convertion_liste_to_farenheit(liste_Celsius)
print("celcius ", liste_Celsius)
print("newlste ", new_liste_f) #[53.6, 68.0, 32.0, 28.4, 73.4, 44.6]