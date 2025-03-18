def function(nom, prenom):
    print("Corps de la fonction 1")
    print("Corps de la fonction 2")
    print("Bonjour ", nom, prenom)
    return "Object Retourne"

print("Pas dans la fonction")

result = function("Paul", "Ernest")
print(result) #Object Retourne

def return_no():
    print("Called")
    #return None

result2 = return_no()
print(result2) #None


print("end")